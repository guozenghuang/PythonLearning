"""
利用互斥锁来解决全局变量在多线程共享中资源竞争的问题
"""


import threading
import time


g_number = 0


def test1(count):
    global g_number
    # 互斥锁上锁
    # 若之前没有上锁，则此处会上锁成功；若已上锁，则会阻塞在此，直至该锁被解锁
    mutex.acquire()
    for i in range(count):
        g_number += 1
    # 解锁
    mutex.release()
    print("g_number in test1 : %d " % g_number)


def test2(count):
    global g_number
    mutex.acquire()
    for i in range(count):
        g_number += 1
    mutex.release()
    print("g_number in test2 : %d " % g_number)


# 创建一个互斥锁，默认没有上锁
mutex = threading.Lock()


def main():

    count = 10000000
    t1 = threading.Thread(target=test1, args=(count,))
    t2 = threading.Thread(target=test2, args=(count,))
    t1.start()
    t2.start()

    # 等待5秒显示结果
    time.sleep(5)
    print("g_number in main : %d " % g_number)


if __name__ == "__main__":
    main()
