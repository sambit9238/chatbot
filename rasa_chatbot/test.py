import requests

ip  = '104.154.194.160'
port = 85
url = f"http://{ip}:{port}/webhooks/rest/webhook"

payload = "{\n    \"sender\": \"sam\",\n    \"message\": \"hello\"\n}"
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
