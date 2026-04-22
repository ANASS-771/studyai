# URL de l'API (remplacer le modèle si besoin)
HF_URL = 'https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2'


headers = {
  'Authorization': f'Bearer {HF_TOKEN}',
  'Content-Type': 'application/json'
}


payload = {
  'inputs': '<votre prompt ici>',
  'parameters': {
    'max_new_tokens': 800,
    'temperature': 0.5,
    'return_full_text': False
  }
}


response = requests.post(HF_URL, headers=headers, json=payload)
result = response.json()   # retourne une liste
text = result[0]['generated_text']
