from PySide2.QtCore import QRunnable



class Worker(QRunnable):
    def __init__(self, *args):
        super(Worker, self).__init__()
        self.resolution = args

    def run(self):
        print("x : ", self.resolution[0]) , print("y : ", self.resolution[1],"\n")        