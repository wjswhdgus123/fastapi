import requests


url = "http://127.0.0.1:8080/execute_command/"
payload = {
    "host": "192.168.219.40",
    "port": 22,  # 일반적으로 22번 포트를 사용합니다.
    "username": "ubuntu",
    "password": "@whdgus123!",
    "command": "ls"
}

response = requests.post(url, json=payload)
print(response.json())
