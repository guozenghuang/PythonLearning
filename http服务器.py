import socket


def client_service(new_socket):
    """为该客户端返回数据"""
    # 1.接收浏览器发来的请求, http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)

    # 2.返回http格式数据
    # 准备发送给浏览器的数据 header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 准备发送给浏览器的数据 body
    response += "<h1>h1h1h1h1</h1>"

    new_socket.send(response.encode("utf-8"))

    new_socket.close()


def main():
    """完成套接字的控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定
    tcp_server_socket.bind(("", 8888))

    # 3.变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4.等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5.为客户端服务
        client_service(new_socket)

    tcp_server_socket.close()
    

if __name__ == "__main__":
    main()
