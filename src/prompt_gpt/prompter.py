import json
import os

class Prompter:
    def __init__(self, open_ai_client):
        self._openai_client = open_ai_client

    def prompt(self, event, context):
        print("prompting")
        prompt = "What is the meaning of life? Explain it to me like i'm 5  keep it short and sweet"
        print(self._openai_client)
        response = self._openai_client.create(prompt)
        print(f"got response {response}")
        message = response.choices[0].message.content
        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }
    
    def create_prompter(openai_client):
        return Prompter(openai_client)