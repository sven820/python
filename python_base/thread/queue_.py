__author__ = "JJ.sven"

import queue

'''queue
1. Queue 先入先出
2. LifoQueue 先入后出
3. PriorityQueue 可设置优先级队列
'''

'''1 Queue 先入先出'''
q = queue.Queue(1)
q.put('dist1')

# 超过容量再存也会卡住
# q.put('dist2')
# q.put_nowait('dist2')
# q.put('dist2', block=False)

print(q.get())

# 为空再取，挂起等着
# print(q.get())
# 为空取，不挂起等待
# try:
#     q.get_nowait()
# print(q.get(block=False, timeout=10))
# except Exception as e:
#     print(e)

'''2 lifoQueue'''
lifoQueue = queue.LifoQueue()
lifoQueue.put(1)
lifoQueue.put(2)
lifoQueue.put(3)
print(lifoQueue.get())
print(lifoQueue.get())
print(lifoQueue.get())

'''3 PriorityQueue'''
priorityQueue = queue.PriorityQueue()
priorityQueue.put((1, 'zz'))
priorityQueue.put((10, 'jj'))
priorityQueue.put((7, 'cc'))

print(priorityQueue.get())
print(priorityQueue.get())
print(priorityQueue.get())
