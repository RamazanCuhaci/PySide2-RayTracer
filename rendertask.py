from PySide2.QtCore import QRunnable, QObject,Signal
from PySide2.QtGui import QColor 
from world.scene import Scene
import sys
sys.dont_write_bytecode = True


class RenderTask(QRunnable, QObject):
    
    updatePercent = Signal()
    

    def __init__(self, x, y_start, y_end, scene,imgBuffer):
        QRunnable.__init__(self)
        QObject.__init__(self)

        self.x = x
        self.y_start = y_start
        self.y_end = y_end
        self.scene : 'Scene' = scene
        self.imgBuffer = imgBuffer
       

    def run(self):
        for y in range(self.y_start, self.y_end):
            for x in range(0, self.x):
                
                ray = self.scene.camera.send_ray(x, y)
                self.scene.rayCount += 1

                color = QColor(0,0,0)
                
                # Find the closest hit point and take its color
                hit_point = None
                min_hit_point = float('inf')

                # Inline the ray tracer class's hit method
                for shape in self.scene.objects:
                    hit_point= shape.hit(ray)
                    if hit_point < min_hit_point and hit_point > sys.float_info.epsilon:
                        min_hit_point = hit_point
                        color = shape.color
                
                self.imgBuffer.setPixelColor(x, y, color)
            self.updatePercent.emit()
       

                
    