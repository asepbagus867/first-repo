import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

print("Status:", response.status_code)
print("Response:")
print(response.json())