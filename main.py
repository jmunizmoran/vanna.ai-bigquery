import warnings
import sys
import json
import config
import bigquery_vanna

warnings.filterwarnings('ignore')

def get_question(question_index): 
    with open(config.questions_json_path) as f:
        questions = json.load(f)
    return questions['questions'][question_index]

try:
    vn = bigquery_vanna.BigQueryVanna(config={'api_key': config.openai_api_key, 'model': config.openai_model})
    vn.connect_to_bigquery(project_id=config.bigquery_project_id, cred_file_path=config.credentials_json_path)
    vn.train_ncaa()

    question_index = int(sys.argv[1]) - 1

    question = get_question(question_index);
    print('Question: ' + question)

    vn.ask(question = question)
except IndexError:
    print('The program expects an integer as the parameter to select the question to ask to the model')

