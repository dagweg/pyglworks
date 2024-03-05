import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from primitives.d3 import Cube
import renderer.primitiveRenderer as pr
import random

class App:

  cube = Cube()

  def __init__(self,width,height,title):
    pg.init()
    pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption(title)
    self.clock = pg.time.Clock()
    glClearColor(0.1,0.1,0.1,1)
    gluPerspective(45,width/height,0.1,500)
    glTranslatef(0,0,-50)
    glRotatef(5,0,0,0)
    self.mainLoop()

  def draw(self):
    pr.Primitive3D.render(self.cube,wireframe=True)
    pass
  
  def mainLoop(self):
    while True:
      self.pygameEventHandler()

      glClear(GL_COLOR_BUFFER_BIT)
      
      self.draw()

      # print(glGetDoublev(GL_MODELVIEW_MATRIX))
      x,y,z,zc = glGetDoublev(GL_MODELVIEW_MATRIX)[3]
      if z < 0:
        rx =random.random()
        print(rx)
        if -3 < x < 3 and -3 < y < 3:
          pg.time.wait(2000)
        else:
          pg.time.wait(10)
        glTranslatef(x+rx if x > 0 else x-rx,0,-50)
      


      # glRotatef(1,45,90,45)
      glTranslatef(0,0,0.35)
      self.clock.tick(120)
      pg.time.wait(10)
      pg.display.flip()

  def pygameEventHandler(self):
    for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_LEFT:
            glTranslatef(0.5,0,0)
          if event.key == pg.K_RIGHT:
            glTranslatef(-0.5,0,0)
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

  