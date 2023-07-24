from fastapi import FastAPI
import socket

app = FastAPI()

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