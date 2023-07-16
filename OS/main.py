from fastapi import FastAPI
import paramiko
import getpass
app = FastAPI()
@app.get("/serverinfo/{ip}/{user}/{pwd}/{cmd}")
def serverinfo(ip: str , user: str, pwd: str, cmd: str ):
     
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    print(ip, user, pwd, cmd)
    server = ip  # 호스트명이나 IP 주소192.
    user = user  
    pwd =  pwd # 암호입력 숨김

    
    cli.connect(server, port=22, username=user, password=pwd)
    if cmd == "cpu":
        stdin, stdout, stderr = cli.exec_command("cat /proc/cpuinfo")
    elif cmd == "mem":
        stdin, stdout, stderr = cli.exec_command("free -g")
    elif cmd == "OS":
        stdin, stdout, stderr = cli.exec_command("cat /etc/os-release")
    elif cmd == "host":
         stdin, stdout, stderr = cli.exec_command("hostname")
    cpu = stdout.readlines()
    cli.close()
    return cpu
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
