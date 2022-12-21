import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(('127.0.0.1', 9002))
print('connection...')
info = ''
while info != 'exit':
    send_mes = input('>>>')
    s.sendall(send_mes.encode())
    if send_mes == 'exit':
        break
    info = s.recv(1024).decode()
    print('服务端:' + info)
s.close()
