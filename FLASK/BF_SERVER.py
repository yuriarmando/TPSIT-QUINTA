#YURI ARMANDO
#SERVER CON DATI
import socket as socket

server_ip = "xxx.x.x.x"
server_port = 8084

def client():
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    c.connect((server_ip,server_port))

    while True:

        body = "username=Yuriarmando&email=yuri.armando@gmail.com&password=1234"
        msg = f"POST http://127.0.0.1:80/register HTTP/1.1\r\nHost: 127.0.0.1:80\r\nConnection: open\r\nContent_Type:application/x-www-form-urlencoded\nContent_Length: {len(body)}\r\n\r\n"+body
        print(f"sending:\n\n{msg}\n\n")
        c.sendall(msg.encode())
        echo_msg = c.recv(4096)
        print(f"ECHO>> {echo_msg}")
        if len(echo_msg) > 0:
            break
    
    c.close()


if __name__ == "__main__":
    client()
