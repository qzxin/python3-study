#task_master.py
#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000

import random, time, queue
from multiprocessing.managers import BaseManager

#send_mask_queue
task_queue = queue.Queue()
#result
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass
#注册queue到网络
QueueManager.register('net_task_queue', callable = lambda : task_queue)
QueueManager.register('net_result_queue', callable = lambda : result_queue)
#绑定端口
manager = QueueManager(address=('', 5000), authkey=b'abc')
#启动Queue
manager.start()
#get 网络共享出的Queue
task = manager.net_task_queue()
result = manager.net_result_queue()
#put 任务进queue
for i in range(10):
    n = random.randint(0, 10000)
    print("Put task 'n = %s'" % n)
    task.put(n)
#从result 队列读取结果
print('Try to get result from queue...')
for i in range(10):
    r = result.get(timeout = 10)
    print('result: %s' % r)
#shutdown
manager.shutdown()
print('master exit.')



















