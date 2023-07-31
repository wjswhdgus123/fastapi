import socket

def is_port_open(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout 설정 (초 단위)
            s.connect((ip, port))
        return True
    except:
        return False