__author__ = "JJ.sven"

'''递归锁， Lock & RLock

如果一个锁的状态是unlocked，调用acquire()方法改变它的状态为locked
如果一个锁的状态是locked，acquire()方法将会阻塞，直到另一个线程调用release()方法释放了锁；
如果一个锁的状态是unlocked调用release()会抛出RuntimeError异常；
如果一个锁的状态是locked，调用release()方法改变它的状态为unlocked。

Lock 一个acquire后接着再acquire就会死锁
我的理解 lock.acquire=>lock.acquire(这里会等待前面锁解锁，但前面那个锁解锁又需要等当前步骤结束后
解锁，但当前lock.acquire又占用着，不会调用后面的解锁，相互等待就死锁了)

RLock 多重锁，同一时刻允许多个线程拿到锁，acquire后登记以下，当前锁count+1，解锁后count-1
- 在同一线程中可用被多次acquire而不死锁。
- 如果使用RLock，那么acquire和release必须成对出现，  
  调用了n次acquire锁请求，则必须调用n次的release才能在线程中释放锁对象
'''

'''补充
- 同步阻塞
当一个线程调用Lock对象的acquire()方法获得锁时，这把锁就进入“locked”状态。
因为每次只有一个线程1可以获得锁，所以如果此时另一个线程2试图获得这个锁，该线程2就会变为“blo同步阻塞状态。
直到拥有锁的线程1调用锁的release()方法释放锁之后，该锁进入“unlocked”状态。
线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。
- 进一步考虑
通过对公共资源使用互斥锁，这样就简单的到达了我们的目的，但是如果我们又遇到下面的情况：
遇到锁嵌套的情况该怎么办，这个嵌套是指当我一个线程在获取临界资源时，又需要再次获取；
如果有多个公共资源，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源；
上述这两种情况会直接造成程序挂起，即死锁，下面我们会谈死锁及可重入锁RLock。
- 死锁概念
所谓死锁： 是指两个或两个以上的进程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，
它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程。
由于资源占用是互斥的，当某个进程提出申请资源后，使得有关进程在无外力协助下，永远分配不到必需的资源而无法继续运行，
这就产生了一种特殊现象死锁。
'''

import threading, time


def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)


if __name__ == '__main__':

    num, num2 = 0, 0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)