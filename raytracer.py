import sys
from PySide2.QtGui import QColor

class RayTracer:

    def __init_(self):
        pass

    def trace(self, ray, scene):
        
        color = QColor(0,0,0)
        hit_point = None
        min_hit_point = float('inf')
        
        for shape in scene.objects:
            hit_point= shape.hit(ray)
            if hit_point < min_hit_point and hit_point > sys.float_info.epsilon:
                min_hit_point = hit_point
                color = shape.color

        return color