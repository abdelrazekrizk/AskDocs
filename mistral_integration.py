import requests

def generate_answer(prompt):
    url = "https://api.mistral.ai/v1/generate"
    payload = {"prompt": prompt, "max_tokens": 300}
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["generated_text"]
    else:
        return f"Error: {response.status_code}, {response.text}"
