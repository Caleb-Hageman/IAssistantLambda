import os
import json
class AppConfiguration:
    def __init__(self):
        self._config = self._get_config()
    
    def _get_config(self):
        if self._is_lambda_runtime():
            return {} # todo fill this out
        else:
            return self._get_dev_config()

    def _is_lambda_runtime(self):
        return True if os.environ.get("AWS_DEFAULT_REGION") else False

    def _get_dev_config(self):
        # Opening JSON file
        f = open('dev_config.json')

        # returns JSON object as 
        # a dictionary
        return json.load(f)

    def get_open_ai_key(self):
        if self._is_lambda_runtime():
            return os.environ.get("OPENAI_API_KEY")
        return self._config.get("OPENAI_API_KEY")
