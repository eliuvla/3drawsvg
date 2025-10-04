from shape import *
from scene import *

import drawsvg as dw 

class Sphere(Shape):
    def __init__(self):
        self.center = (0,0,0)
        self.color_stroke = (0,0,0)
        self.color_fill = (255,255,255)
        self.radius = 10

    def draw(self, scene = Scene()):
        scene.canvas.append(dw.Circle(self.center[0], self.center[1], self.radius))
