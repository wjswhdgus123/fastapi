from fastapi import FastAPI
from app.portcheck import is_port_open 
from  app.sshcomm import execute_ssh_command

app = FastAPI()


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