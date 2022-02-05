class PythonMQ(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, num):
        # キューの最後尾に値を追加
        self.queue.append(num)

    def dequeue(self):
        # キューの最前値を取り出す
        # 取り出した値を活用可能
        return self.queue.pop(0)

    def adjustQueueSize(self, num = 1):
        # 0で値を格納
        for i in range(num):
            self.queue.append(0)

    def updateQueue(self, index, num):
        # 指定されたインデックスの値を更新
        self.queue[index] = num

    def getQueue(self):
        # キューを返す
        return self.queue

    def getQueueSize(self):
        # キューサイズを返す
        return len(self.queue)

    def checkQueue(self):
        # キューの中身を確認
        print('---------------------------------------------------------')
        print('QueueSize:' + str(len(self.queue)))
        print('Final' +'[' + str(len(self.queue)-1) + '] > ' + str(self.queue[::-1]) + ' > Front[0]')
        print('---------------------------------------------------------')
