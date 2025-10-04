import drawsvg as dw 
from shapes.shapes import *


class Scene():
    def __init__(self, width = 100, height = 100 , id_prefix = 'unique_name', camera = None):

        self.width = width
        self.height = height
        self.id = id_prefix
        self.name = "example"
        self.camera = camera 

        self.objects: list[Shape] = []

        self.canvas = dw.Drawing(width, height, origin=(0, 0), id_prefix= self.id)

    def draw(self):
        for object in self.objects:
            object.draw(self)

    def save(self):
        self.canvas.save_svg(self.name+".svg")

