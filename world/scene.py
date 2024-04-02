import json
from utility.vector import*
from objects.shapes import Sphere
from world.camera import Camera
from utility.ray import Ray
import os

class Scene:

    def __init__(self,scene_path):
        self.objects = []
        self.buildScene(scene_path)
        self.camera : Camera

    def addObject(self,obj):
        self.objects.append(obj)

    def addCamera(self,cam):
        self.camera = cam

    def buildScene(self,scene_path):

        
        relative_path = os.path.join(os.path.dirname(__file__), scene_path)

        with open(relative_path, 'r') as file:
            json_data = json.load(file)


        camera_data = json_data["camera"]
        render_data = json_data["renderSettings"]
        camera = Camera(
            camera_data["posX"],
            camera_data["posY"],
            camera_data["posZ"],
            camera_data["focalLength"],
            render_data["xres"],
            render_data["yres"],
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


        

