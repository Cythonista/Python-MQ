import PythonMQ as pymq

def main():
    mq = pymq.PythonMQ()

    # キューに格納
    mq.enqueue(1)
    mq.enqueue(2)
    mq.enqueue(3)

    # キューの中身を確認 [3,2,1]
    mq.checkQueue()

    # 先頭の値をデキュー
    mq.dequeue()

    # 取り出して利用することも可能
    # num = mq.dequeue()
    # print(num)

    # キューの中身を確認 [3,2]
    mq.checkQueue()

    # キューの中身を更新 [99,2]
    mq.updateQueue(1, 99)
    mq.checkQueue()

    # キューサイズ取得
    print(mq.getQueueSize())
    # キューそのものを取得
    print(mq.getQueue())

if __name__ == '__main__':
    main()
