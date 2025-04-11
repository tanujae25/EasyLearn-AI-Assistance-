import requests

url = "http://127.0.0.1:5000/chat"

payload = {"message": "Hello Gemini"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)

