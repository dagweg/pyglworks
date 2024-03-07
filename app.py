import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from primitives.d3 import Cube, Cylinder
import renderer.primitiveRenderer as pr
import random

class App:

  cube = Cube()
  x_offset = 0
  y_offset = 0
  x_translate = 0

  def __init__(self,width,height,title):
    pg.init()
    pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption(title)
    gluPerspective(45,width/height,0.1,500)
    self.clock = pg.time.Clock()
    glClearColor(0.1,0.1,0.1,1)
    glTranslatef(0,0,-50)
    glRotate(45,1,0,0)
    for i in range(3):
      self.mainLoop()

  def draw(self):
    pr.Primitive3D.render(self.cube,wireframe=True)
    pass
  
  def mainLoop(self):

    

    while True:
      self.pygameEventHandler()

      glClear(GL_COLOR_BUFFER_BIT)
      
      # self.draw()
      cylinder = Cylinder(height=10,sides=50,radius=10)
      
      # x,y,z,zc = glGetDoublev(GL_MODELVIEW_MATRIX)[3]
      # if z < 0:
      #   if -3 < x < 3 and -3 < y < 3:
      #     pg.time.wait(1000)
      #     break
      #   else:
      #     pg.time.wait(10)
          
      #   glTranslatef(-self.x_offset,0,-50)
      #   self.x_offset = 0
      

      glRotatef(1,45,45,0)
      # glTranslatef(self.x_translate,0,0.5)
      self.clock.tick(120)
      pg.time.wait(10)
      pg.display.flip()

  def pygameEventHandler(self):
    for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_LEFT:
            self.x_offset += 0.1
            self.x_translate = 0.1
          if event.key == pg.K_RIGHT:
            self.x_offset -= 0.1
            self.x_translate = -0.1


        if event.type == pg.KEYUP:
          if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
            self.x_translate = 0

        # print(self.x_offset)

          # if event.key == pg.K_UP:
          #   glTranslatef(0,-0.5,0)
          # if event.key == pg.K_DOWN:
          #   glTranslatef(0,0.5,0)

        if event.type == pg.MOUSEBUTTONDOWN:
          if event.button == 4:
            glTranslate(0,0,0.1)
          if event.button == 5:
            glTranslate(0,0,-0.1)

        


if __name__=='__main__':
  app = App(800,600,'Xg Engine Pro 2024')

  