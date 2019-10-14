import socket


def send_msg(udp_socket):
    """"发送消息"""
    # 获取要发送的内容
    dest_addr = input("请输入目标IP:")
    dest_port = int(input("请输入目标port:"))
    send_data = input("请输入发送内容:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_addr, dest_port))


def recev_msg(udp_socket):
    """接收消息"""
    recv_msg = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_date[1]),recv_date[0].decode("utf-8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("", 9999))

    # 循环处理事务
    while True:
        # 发送消息
        send_msg(udp_socket)

        # 接收消息
        recev_msg(udp_socket)


if __name__ == "__main__":
    main()