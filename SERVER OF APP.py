import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(("127.0.0.1",5000))
s.listen(5)
conn,addr=s.accept()
print("Got Connection From",addr)
while True:
    print(conn.recv(1024))
    data="HARSHDEEP=>"+input("")
    conn.send(bytes(data, encoding="utf-8"))
   
   

