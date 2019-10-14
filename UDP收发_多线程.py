import socket
import threading


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("请输入要发送的数据:")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))


def main():

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(("", 8888))

    # 获取对方ip
    dest_ip = input("请输入对方ip:")
    dest_port = int(input("请输入对方端口:"))

    # 进行聊天
    t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    t2 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
