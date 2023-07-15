from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/check_port/{ip}/{port}")
def check_port(ip: str, port: int):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 연결 시간 초과를 설정합니다. 필요에 따라 조정할 수 있습니다.
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return {"message": f"Port {port} on {ip} is open."}
        else:
            return {"message": f"Port {port} on {ip} is closed."}
    except socket.error as e:
        return {"message": f"An error occurred: {e}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 