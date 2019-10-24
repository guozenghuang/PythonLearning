import socket
import re
import threading


def client_service(new_socket):
    """为该客户端返回数据"""
    # 1.接收浏览器发来的请求, http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024)

    request_lines = request.splitlines()
    print("")
    print(">"*20)
    print(request_lines)
    # print(request)

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

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
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.绑定
    tcp_server_socket.bind(("", 8888))

    # 3.变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4.等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5.为客户端服务
        p = threading.Thread(target=client_service, args=(new_socket,))
        p.start()

        new_socket.close()
        # client_service(new_socket)

    tcp_server_socket.close()
    

if __name__ == "__main__":
    main()
