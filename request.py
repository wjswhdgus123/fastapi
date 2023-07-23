import requests

def serverinfo (host,port,id,pw,cmd):
    url = "http://localhost:8000/execute_command/"
    payload = {
        "host": host,
        "port": 22 , # 일반적으로 22번 포트를 사용합니다.
        "username": id, 
        "password": pw,
        "command": cmd
        }
    print(payload)
    return requests.post(url, json=payload)

serverinfo("plna01",22,"ubuntu","@whdgus123!","ls")
    
