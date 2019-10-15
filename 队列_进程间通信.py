import multiprocessing


def download_data(que):
    """下载数据"""
    # 模拟数据
    data = [11, 22, 33, 44, 55]

    # 向队列中写入数据
    for temp in data:
        que.put(temp)

    print("已下载完数据并存入队列中")


def analysis_data(que):
    """处理数据"""
    waitting_aanlysis_data = list()
    # 从队列中获取数据
    while True:
        data = que.get()
        waitting_aanlysis_data.append(data)

        print("处理数据:%d" % data)

        if que.empty():
            break



def main():
    # 创建一个队列
    que = multiprocessing.Queue()

    # 创建多个进程，将队列的引用当作实参进行传递
    p1 = multiprocessing.Process(target=download_data, args=(que,))
    p2 = multiprocessing.Process(target=analysis_data, args=(que,))
    p1.start()
    p2.start()



if __name__ == "__main__":
    main()
