import sys
sys.dont_write_bytecode = True
from utility.vector import *
from utility.ray import Ray

class Camera:

    def __init__(self,posX,posY,posZ,focal_length, res_x, res_y):
        self.eye = Point3f(posX,posY,posZ)
        self.look_at = Point3f(0,0,0)
        self.direction = Vector3f(0,0,-1)
        self.up = Vector3f(0,1,0)

        self.res_x = res_x
        self.res_y = res_y

        self.aspect_ratio = res_x/res_y

        self.focal_length = focal_length
        

    def send_ray(self,x,y):
        
        # Convert pixel coordinates to NDC
        pixel_ndc_x = (2* x/self.res_x - 1)* self.aspect_ratio
        pixel_ndc_y = 1 - (2*y/self.res_y)

        ray_direction = self.direction + Vector3f(pixel_ndc_x,pixel_ndc_y,0)

        ray_direction = ray_direction.normalize()

        return Ray(self.eye, ray_direction)

