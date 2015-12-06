#task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass
#从网络中注册queue（只是获取，所以仅提供name）
QueueManager.register('net_task_queue')
QueueManager.register('net_result_queue')
#连接server
server_addr,server_port = '127.0.0.1', 5000
server_key = b'abc'
manager = QueueManager(address=(server_addr, server_port), authkey=server_key)
manager.connect()
#获取网络中queue
task = manager.net_task_queue()
result = manager.net_result_queue()
#从task读取任务，处理后，放到result
for i in range(20):
    try:
        n = task.get(timeout = 1)
        print("running '%d * %d'..." % (n, n))
        r = ('%d * %d = %d' % (n, n, n*n))
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')
#done
print('task worker exit.')




