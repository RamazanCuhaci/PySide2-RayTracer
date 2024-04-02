from PySide2.QtCore import QRunnable
import time

class RenderTask(QRunnable):

    def __init__(self, x, y, scene, paintWidget,tracer):
        super(RenderTask, self).__init__()
        self.x = x
        self.y = y
        self.scene = scene
        self.paintWidget = paintWidget
        self.ray_tracer = tracer

    def run(self):
        ray = self.scene.camera.send_ray(self.x, self.y)
        color = self.ray_tracer.trace(ray, self.scene, self.paintWidget)
        self.paintWidget.imgBuffer.setPixelColor(self.x, self.y, color)
        time.sleep(1)