from math import pi,cos,sin
from OpenGL.GL import *

class Cylinder:
  def __init__(self,height=10,sides=5,radius=5):
    self.upperbase = []
    self.lowerbase = []
    self.edges = []

    half_height = height//2
    angle_step= (2 * pi) / sides

    for i in range(sides):
      angle = angle_step * i
      x = radius * cos(angle)
      z = radius * sin(angle)

      self.upperbase.append((x,half_height,z))
      self.lowerbase.append((x,-half_height,z))

    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    for x,y,z in self.upperbase:
      glVertex3f(x,y,z)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    for x,y,z in self.lowerbase:
      glVertex3f(x,y,z)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    for i in range(len(self.upperbase)):
      glVertex3fv(self.upperbase[i])
      glVertex3fv(self.lowerbase[i])
    glEnd()





    

