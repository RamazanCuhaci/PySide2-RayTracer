
from math import sqrt
from utility.ray import Ray
from PySide2.QtGui import QColor
from utility.vector import Point3f
from utility.ray import Ray
class Sphere():
    
    def __init__(self, radius, posX, posyY, posZ , r, g, b):
        
        self.position = Point3f(posX,posyY,posZ)
        self.color = QColor(r,g,b)
        self.radius = radius

    
    def hit(self, ray:Ray):
        
        temp = ray.origin - self.position
        a = ray.direction.dot(ray.direction)
        b = 2.0 * temp.dot(ray.direction)
        c = temp.dot(temp) - (self.radius*self.radius)
        disc = b * b - 4.0 * a * c

        if disc < 0:
            return -1.0
        else:
            e = sqrt(disc)
            denom = 2.0 * a
            t1 = (-b - e) / denom
            t2 = (-b + e) / denom 
            return min(t1,t2)
