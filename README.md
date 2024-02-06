# PoC use of Vanna.ai and Bigquery

## 📝 Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Project Configuration](#project_configuration)
- [Run](#run)

## About <a name = "about"></a>

This is a quick-and-dirty proof-of-concept of the use of [Vanna.ai](https://vanna.ai/) to talk with data stored in [Google BigQuery](https://cloud.google.com/bigquery?hl=en).

We will be exploring the [NCAA Basketball public dataset](https://console.cloud.google.com/marketplace/product/ncaa-bb-public/ncaa-basketball) using natural language.

>_This dataset contains data about NCAA Basketball games, teams, and players. Game data covers play-by-play and box scores back to 2009, as well as final scores back to 1996. Additional data about wins and losses goes back to the 1894-1895 season for some teams. All data runs through the end of the 2017-2018 season_ 
Source: Google Cloud

## Prerequisites <a name = "prerequisites"></a>

### Google Cloud Access

We will be exploring the NCAA Basketball public dataset in Google Cloud, so we need a Google Cloud account. If you don't have one, I recommend that you sign up for the free tier where (as per today) they give you 300USD that you can use to test Google Cloud products for 4 months. [More info here](https://cloud.google.com/free)

### Google BigQuery Project

Once we have access to Google Cloud we need to create a BigQuery project in Google Cloud and import the NCAA Basketball public datasource.

These are the steps you need to follow to complete this step:
* Log into the [Google Cloud Console](https://console.cloud.google.com/) and, in the upper search box, enter "BigQuery"
* You need to select the Google Cloud project to work with. If you don't have any, go and create one. [Guide to create a project in GCP](https://developers.google.com/workspace/guides/create-project). I've used `vanna-bigquery-poc` name for this project.
* Once you have a project selected, is time to add the public NCAA Basketball datasource. For doing this, you need to click the "+ADD" button on the top of the explorer panel.
![Add a datasource to a BigQuery Project](/resources/images/add_datasource.png)
* Click on the "Analytics Hub - Discover and subscribe to public, commercial or privately shared datasets"
![Analytics Hub](/resources/images/analytics_hub.png)
* Search for the "NCAA Basketball" datasource and click the "Add Dataset to Project" button and accept the default options
![Add NCAA Dataset](/resources/images/add_dataset.png)
* Now your dataset is imported into your BigQuery Project:
![Dataset added](/resources/images/dataset_added.png)

### Google Cloud credentials.json

In order to connect your PoC to Google Cloud you need to get create credentials for a service account. You can follow the instructions here: [Get Credentials for Service Account](https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account)

Once you finish this step, save the .json file as it will be needed later on.

### Import python required libraries

In order to run this PoC you need to install some python libraries:

```
pip install vanna
pip install db-dtypes
pip install openai
pip install chromadb
```

## Project Configuration <a name = "project_configuration"></a>

There are some configuration steps needed to run this PoC
* Replace the `credentials.json` in the project resources folder with the one that you have generated previously in the prerequisite step.
* Open the `config.py` file and set the following values:
  - `bigquery_project_id` with the name of the Google Cloud Project where you have upload the NCAA Basketball datasource. E.g. `vanna-bigquery-poc`
  - `openai_api_key` this PoC uses OpenAI as the LLM to create the SQL queries to the datasource, put here your OpenAI API key.

## Run it! <a name = "run"></a>

The project has a file called `questions.json` that contains some examples of questions that you can make to the model.

To run one of these questions you can run this command:

```
python main.py 1
```

This will take the first question in the file: `Who is the player with more points if you consider all registered matches and how many points did he score during his carreer?` and the answer should be: `Justin Robinson 2915`

You can add as many questions as you like into the `questions.json` file and use the question index, for example, if you want to run the 8th question in the file, you can run:

```
python main.py 8
```