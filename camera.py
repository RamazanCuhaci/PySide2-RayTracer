from mathlib.vector import *
from ray import Ray

class Camera:

    def __init__(self,posX,posY,posZ,focal_length,x_res,y_res):
        self.eye = Point3f(posX,posY,posZ)
        self.look_at = Point3f(0,0,0)
        self.direction = Vector3f(0,0,-1)
        self.up = Vector3f(0,1,0)

        self.focal_length = focal_length
        
        self.x_res = x_res
        self.y_res = y_res

    def send_ray(self,x,y,height,width):
        
        # Convert pixel coordinates to NDC
        pixel_ndc_x = (2* x/width) - 1
        pixel_ndc_y = 1 - (2*y/height)

        ray_direction = self.direction + Vector3f(pixel_ndc_x,pixel_ndc_y,0)

        ray_direction = ray_direction.normalize()

        return Ray(self.eye, ray_direction)

