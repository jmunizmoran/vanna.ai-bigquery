import config
import json

from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
from vanna.openai.openai_chat import OpenAI_Chat

class BigQueryVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)
        self.__training_data = self.__load_training_data()
        
    def __load_training_data(self):
        with open(config.training_model_json_path) as f:
            training = json.load(f)
        return training['training']

    def train_ncaa(self):
        df_information_schema = self.run_sql(f"SELECT * FROM `{config.bigquery_project_id}.ncaa_basketball.INFORMATION_SCHEMA.COLUMNS`")
        plan = self.get_training_plan_generic(df_information_schema)
        self.train(plan=plan)

        for training_data in self.__training_data:
            if training_data['type'] == 'documentation':
                self.train(documentation = training_data['value'])
            elif training_data['type'] == 'sql':
                sql = training_data['value'].replace('{bigquery.project.id}', config.bigquery_project_id)
                self.train(question=training_data['question'], sql=sql)
            else:
                print('Type: ' + training_data['type'] + ' not supported')

