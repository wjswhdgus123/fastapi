import requests

api_url = "http://api.bestpath.co.kr/"

def server_comm(ip: str , username: str, pw: str, command: str):
    url = f'{api_url}server'
    body = {
        'ip': ip,
        'username': username,
        'pw': pw,
        'command': command  
    
    }
    response = requests.get(url, params=body)

    print (response.json())




    return None

server_comm('192.168.219.40','ubuntu','@whdgus123!','cat /proc/cpuinfo|grep processor|tail -1|awk -F \':\' \'{print $2+1}\'')