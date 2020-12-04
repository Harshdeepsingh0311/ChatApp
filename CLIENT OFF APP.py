import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect(("127.0.0.1",5000))
while True:
    data="CLIENT=>"+input("")
    s.send(bytes(data, encoding="utf-8"))
    print(s.recv(1024))
    
    
   
