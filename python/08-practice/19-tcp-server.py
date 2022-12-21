import socket 

print('正在连接中...')

def dealclient(sock, addr):
    # 接受客户端发送的信息
    info = sock.recv(1024).decode()
    #循环判断
    while info !='exit':
        # 打印客户端发的信息
        print('客户端:'+info)
        #输入服务端发的信息
        send_mes = input('>>>')
        # 服务端发送信息
        sock.send(send_mes.encode())
        # 如果发送信息是exit 
        if send_mes == 'exit':
            break
        # 接受信息
        info = sock.recv(1024).decode()
    sock.close()

if __name__ == '__main__':
    # 创建一个socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9001))

    # 监听端口
    s.listen(1)
    # 阻塞等待客户连接
    sock, addr = s.accept()
    # 传入函数中,处理逻辑
    dealclient(sock, addr)
