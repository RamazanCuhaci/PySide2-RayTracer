import sys
sys.dont_write_bytecode = True
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtConcurrent import *
from rendertask import RenderTask
from world.scene import Scene
import os


class PaintWidget(QWidget):
    def __init__(self, width, height, parent=None):
        super(PaintWidget, self).__init__(parent=parent)
        self.width = width
        self.height = height

        # setup an image buffer
        self.imgBuffer = QImage(self.width, self.height, QImage.Format_ARGB32_Premultiplied)
        self.imgBuffer.fill(QColor(0, 0, 0))


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.drawImage(0, 0, self.imgBuffer)


    def sizeHint(self):
        return QSize(self.width, self.height)


class PyTraceMainWindow(QMainWindow):
    def __init__(self, qApp, scene: Scene):
        super(PyTraceMainWindow, self).__init__()

        self.qApp = qApp
        self.width = scene.camera.res_x
        self.height = scene.camera.res_y
        self.gfxScene = QGraphicsScene()
        self.scene = scene
        self.threadPool = QThreadPool.globalInstance()
        self.threadCount = self.threadPool.maxThreadCount()
        self.processPercentage = 0

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"PyTrace")
        self.resize(self.width + 25, self.height + 25)
        self.setWindowTitle("Implement Ray Sphere intersection")
        self.setStyleSheet("background-color:black;")
        self.setAutoFillBackground(True)

        # set centralWidget
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName(u"CentralWidget")

        # create a layout to hold widgets
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # setup the gfxScene
        self.gfxScene.setItemIndexMethod(QGraphicsScene.NoIndex)

        # create a paint widget
        self.paintWidget = PaintWidget(self.width, self.height)
        self.paintWidget.setGeometry(QRect(0, 0, self.width, self.height))
        self.paintWidgetItem = self.gfxScene.addWidget(self.paintWidget)
        self.paintWidgetItem.setZValue(0)

        # create a QGraphicsView as the main widget
        self.gfxView = QGraphicsView(self.centralWidget)
        self.gfxView.setObjectName(u"GraphicsView")

        # assign our scene to view
        self.gfxView.setScene(self.gfxScene)
        self.gfxView.setGeometry(QRect(0, 0, self.width, self.height))

        # add widget to layout
        self.horizontalLayout.addWidget(self.gfxView)

        # set central widget
        self.setCentralWidget(self.centralWidget)

        # setup a status bar
        self.statusBar = QStatusBar(self)
        self.statusBar.setObjectName(u"StatusBar")
        self.statusBar.setStyleSheet("background-color:gray;")
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready...")



    def renderScene(self):
        print("Updating buffer...")

        intial_time = QTime.currentTime()

        self.threadCount -= 8 # Subtract 8 threads from the total thread count

        # I divide the height of the image to the number of threads
        # and assign each thread a portion of the image to render

        for i in range(0, self.threadCount):
            
            stride = self.height // self.threadCount
            
            # I pass the image buffer to the worker thread
            # I tried to many different ways to set pixel color 
            # Another way that i tried is to emit a signal in the worker thread and update the buffer in the main thread
            # But passing the image buffer is the fastest way to set pixel color (although i don't know this is the most correct way to do it)
            # Almost 2 times faster than the signal way
            thread = QThread()
            worker = RenderTask(self.width, 0+(i*stride), stride+(i*stride), self.scene, self.paintWidget.imgBuffer)
            worker.updatePercent.connect(self.updatePercent)
            self.threadPool.start(worker)
            
            self.paintWidget.update()
            self.qApp.processEvents()

            self.statusBar.showMessage("Rendering... " +"{:.2f}%".format(self.processPercentage))
            
    
        self.threadPool.waitForDone()
        ending_time = QTime.currentTime()

        self.showStatistics(intial_time,ending_time)

    def updatePercent(self):
        self.processPercentage += 100 / (self.height)

    def showStatistics(self,initial_time,ending_time):
        print("Threads : " + str(self.threadCount) +  
                                   " | Cores in CPU: "+ str(os.cpu_count())+ 
                                   " | Render time: " + str(initial_time.msecsTo(ending_time)) + "ms"+  
                                     " | Rays: " + str(self.scene.rayCount) )

        self.statusBar.showMessage("Threads : " + str(self.threadCount) +  
                                   " | Cores in CPU: "+ str(os.cpu_count())+ 
                                   " | Render time: " + str(initial_time.msecsTo(ending_time)) + "ms"+  
                                     " | Rays: " + str(self.scene.rayCount)+
                                     " | Objects in scene : " + str(len(self.scene.objects)))

        


    
    

        

