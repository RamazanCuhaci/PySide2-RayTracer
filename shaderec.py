# This class keep for the shading record for the ray tracing process
# I saw this approach in the book "Ray Tracing from Ground Up" by Kevin Suffern
# This class is not much useful now but it will be useful in the future
# So i want add from the beginning

from PySide2.QtGui import QColor
from mathlib.vector import Point3f

class ShadeRec:

    def __init__(self):
        self.color = QColor(0,0,0)
        self.hit_an_object = False
        self.hit_point = Point3f(0,0,0)
