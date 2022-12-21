import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9002))
print('wait...')
while True:
    data, addr = s.recvfrom(1024)
    print('客服端:' + data.decode())
    if data.decode() == 'exit':
        break
    info = input('>>>')
    s.sendto(info.encode(),addr)
s.close()
