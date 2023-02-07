import requests
import webbrowser

model_engine = "image-alpha-001"
prompt = "generate an image of the comparison between using AI and not using AI"
size =  "1024x1024"

response = requests.post("https://api.openai.com/v1/images/generations", 
headers={"Authorization": "Bearer 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"},
json={"model": model_engine, "prompt": prompt, "size": size})

if response.status_code == 200:
    image_url = response.json()["data"][0]["url"]
    print(image_url)
    webbrowser.open(image_url, new=2)
else:
    print("Request failed with status code ", response.status_code)
