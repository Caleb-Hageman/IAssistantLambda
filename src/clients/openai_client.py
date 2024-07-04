from openai import OpenAI

class OpenaiClient:
    def __init__(self, client):
        self._client = client
        self._model="gpt-3.5-turbo"
        self._max_tokens = 100
    
    def create(self, prompt):
        print(f"trying to create prompt {prompt}")
        return self._client.chat.completions.create(model=self._model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=self._max_tokens)

    def create_openai_client(app_configuration):
        openai_key = app_configuration.get_open_ai_key()
        openai_client = OpenAI(
            # This is the default and can be omitted
            api_key=openai_key
        )
        return OpenaiClient(openai_client)