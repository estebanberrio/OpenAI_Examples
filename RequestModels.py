import requests
import json

headers = {
  'Authorization': 'Bearer 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'
}

response = requests.get('https://api.openai.com/v1/models', headers=headers)

if response.status_code == 200:
    models = response.json()
    print(json.dumps(models, indent=2))
else:
    print(f"Request failed with status code {response.status_code}")






