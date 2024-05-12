from Display import Display
from Entity import Entity


class Wall(Display,Entity):
    Instances:list["Wall"]=[]
    def __init__(self, coord, radius, color="white",*args,**kwargs):
        super().__init__("wall.png", coord, radius, color,*args,**kwargs)