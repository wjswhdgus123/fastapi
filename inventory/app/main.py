from fastapi import FastAPI
import paramiko
import socket

app = FastAPI()


def execute_ssh_command(hostname, port, username, password, command):
    # SSH 클라이언트 객체 생성
    ssh = paramiko.SSHClient()

    # 호스트 키를 검사하지 않고 자동으로 추가
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # SSH 서버에 접속
        ssh.connect(hostname=hostname, port=port, username=username, password=password)

        # 명령어 실행
        stdin, stdout, stderr = ssh.exec_command(command)

        # 실행 결과 출력
        print("=== Command Output ===")
        print(stdout.read().decode())
        print("=== Command Error (if any) ===")
        print(stderr.read().decode())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # SSH 세션 종료
        ssh.close()

# SSH 접속 정보
#hostname = '192.168.219.77'
#port = 22  # 일반적으로 SSH는 22번 포트를 사용합니다.
#username = 'ubuntu'
#password = '@whdgus123!'  # 또는 SSH Key를 사용할 수도 있습니다.

# 실행할 명령어 (예: ls 명령어 실행)
#command = 'cat /proc/cpuinfo |grep "model name"|tail -1|awk -F \':\' \'{print $2}\''

# SSH로 명령어 실행
#execute_ssh_command(hostname, port, username, password, command)
#command = 'free -g'

#execute_ssh_command(hostname, port, username, password, command)

def is_port_open(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout 설정 (초 단위)
            s.connect((ip, port))
        return True
    except:
        return False
    
@app.get("/check_port/")
def check_port(ip: str, port: int):
    if is_port_open(ip, port):
        return {"message": f"Port {port} is open on {ip}"}
    else:
        return {"message": f"Port {port} is not open on {ip}"}
    
@app.get("/cpuinfo/")
def CPUCoreinfo(hostname: str, port: int, username: str, password: str, command: str):
    command='cat /proc/cpuinfo  |grep "model name" |awk -F \':\' \'{print $2}\'|tail -1'
    if execute_ssh_command(hostname, port, username, password, command):
        return {"message": f"Port {port} is open on {hostname}"}
    else:
        return {"message": f"Port {port} is not open on {hostname}"}