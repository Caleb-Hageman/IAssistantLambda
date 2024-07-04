from src.clients.openai_client import OpenaiClient
from src.configuration.app_configuration import AppConfiguration
from src.prompt_gpt.prompter import Prompter

app_configuration = AppConfiguration()
openai_client = OpenaiClient.create_openai_client(app_configuration)

def lambda_handler(event, context):
    print("hello world")
    response = do_the_thing(event, context)
    print(f"got result {response}")

def do_the_thing(event, context):
    prompter = Prompter.create_prompter(openai_client)
    return prompter.prompt(event, context)

lambda_handler(None, None)

