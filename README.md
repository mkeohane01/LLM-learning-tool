# Hosting Flask Application using Azure

[![Continuous Integration](https://github.com/mkeohane01/LLM-learning-tool/actions/workflows/main.yml/badge.svg)](https://github.com/mkeohane01/LLM-learning-tool/actions/workflows/main.yml)

Here is the [video link](https://youtu.be/q4MmATmijz8) of my project run down.

## Prompt Engineering Sandbox for LLM Education

This project contains a cloud-hosted application to study Large Language Models by breaking up prompt engineering in to 5 parts. In this app, users construct their prompt with: Role, Context, Style, Task, and Constraints clearly listed with an example for each.

The application can be found here: https://prompt-engineering-sandbox.azurewebsites.net/ 

## Use

To deploy this application locally, you can either build and deploy the docker image:
```bash
docker build -t flask-llm-app .
docker run -p 5000:5000 flask-llm-app
```
or you can install the requirements (using a venv) and run the flask server directly.
```bash
pip install -r requirements.txt
flask run
```

For both of these cases you will need a .env file with these three items defined:
```
FLASK_APP=app
FLASK_ENV=<development or production>
OPENAI_API_KEY=<OpenAI api key>
```

## Application Design

This application is powered through flask. There are two main endpoints, each which return an HTML template to be rendered on the front end. First, there is just a get endpoint to display the main screen giving users text inputs for their prompt. Next the other endpoint is called on submit and pushes the user to the results page.

The application is powered by OpenAI by using their GPT-3.5-turbo enginee to generate reponses. I plan on adding options to choose various models in the future including local hosted ones such as LLAMA or FALCON.

This application is then hosted through Azure by using a Docker image hosted through DockerHub. The image I am hosting can be found at mkeohane01/llm-learning-tool:latest. The Azure WebApp is connected directly to this image allowing continous deployment on updates to the image. Also I set enviornmental variables and other features in the Azure service directly.

## Dependencies

The main two packages this application depends on are Flask and OpenAI. Specific versions and subpackages can be found in requirements.txt

## Future Use and Recommendations

I belive many people will benefit from more tools where they can hands-on learn about LLMs and their use cases. While this is just a simple framework for prompt engineering, it can be expanded a variety of ways. Firstly, adding multiple model options to choose from will allow users to test and use options and choose which ones are the best for their task. Another improvement for the tool is to give feedback to the users about where they can improve on their prompts. Finally a more user friendly front end and more information about how these tools work will also improve the educational tool for LLMs.