import json
import sys
from mathlib.vector import*
from shapes import Sphere
from camera import Camera
from ray import Ray
from PySide2.QtGui import QColor

class Scene:

    def __init__(self,scene_path):
        self.objects = []
        self.buildScene(scene_path)
        self.camera : Camera

    def addObject(self,obj):
        self.objects.append(obj)

    def addCamera(self,cam):
        self.camera = cam

    def hit_objects(self,ray:Ray):
        
        color = QColor(0,0,0)
        hit_point = None
        min_hit_point = float('inf')
        
        for shape in self.objects:
            hit_point= shape.hit(ray)
            if hit_point < min_hit_point and hit_point > sys.float_info.epsilon:
                min_hit_point = hit_point
                color = shape.color

        return color
                 

    def buildScene(self,scene_path):

        with open(scene_path, 'r') as file:
            json_data = json.load(file)

        camera_data = json_data["camera"]
        render_data = json_data["renderSettings"]

        camera = Camera(
            camera_data["posX"],
            camera_data["posY"],
            camera_data["posZ"],
            camera_data["focalLength"],
            render_data["xres"],
            render_data["yres"]
        )

       
        self.addCamera(camera)

        spheres = json_data["spheres"]
        
        for sphere_data in spheres:
            color_data = sphere_data["color"]
            
            sphere = Sphere(
                sphere_data["radius"],
                sphere_data["posX"],
                sphere_data["posY"],
                sphere_data["posZ"],
                color_data["r"], color_data["g"], color_data["b"]
            )
            self.objects.append(sphere)


        

