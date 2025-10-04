import drawsvg as dw 

class Scene():
    def __init__(self, width = 100, height = 100 , id_prefix = 'unique_name', camera = None):

        self.width = width
        self.height = height
        self.name = id_prefix
        self.camera = camera 

