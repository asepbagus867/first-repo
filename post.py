import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Hello World",
    "body": "Testing public API",
    "userId": 1,
}

response = requests.post(
    url,
    json=payload,
    timeout=10,
)

print("Status:", response.status_code)
print("Response:")
print(response.json())