from fastapi import FastAPI
import uvicorn
import paramiko

app = FastAPI()

@app.get("/server")
async def serverinfo(ip: str,username: str, pw: str, command: str  ):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip , username=username , password=pw )
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode()

    # 실행 결과 출력
    print("=== Command Output ===")
    print(stdout.read().decode())
    

    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

