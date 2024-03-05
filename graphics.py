from typing import Tuple
from OpenGL.GL import *

class Color:
    def __init__(self):
       self.color = glColor3f(0,0,0)
    def getColor(self):
       return self.color
    def setColor(self,x,y,z):
       self.color = glColor3f(x,y,z)


class Graphics:
  def __init__(self):
    pass


  def drawTri(x,y,z,c:Color):
    pass