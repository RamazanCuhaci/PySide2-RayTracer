from worker import Worker
from PySide2.QtCore import *

threadCount = 4
threadPool = QThreadPool()


for i in range(threadCount):
    worker = Worker(0,4)
    worker = Worker(4,4)
    worker = Worker(0,8)
    worker = Worker(4,8)
    threadPool.start(worker)


