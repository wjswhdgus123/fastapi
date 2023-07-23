from fastapi import FastAPI, HTTPException
import paramiko

app = FastAPI()

@app.post("/execute_command/")
async def execute_command(host: str, port: int, username: str, password: str, command: str):
    try:
        # SSH 클라이언트 생성
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # SSH 서버에 접속
        client.connect(hostname=host, port=port, username=username, password=password)

        # 명령어 실행
        stdin, stdout, stderr = client.exec_command(command)

        # 실행 결과 가져오기
        output = stdout.read().decode()
        error = stderr.read().decode()

        # 접속 종료
        client.close()

        if error:
            raise HTTPException(status_code=500, detail=f"Error executing command: {error}")

        return {"output": output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))