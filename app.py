import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pywavefront import Wavefront
import numpy as np
from collections import deque
from numpy.linalg import *
import random

vertices = (
  (1,1,-1),
  (-1,1,-1),
  (-1,-1,-1),
  (1,-1,-1),

  (1,1,1),
  (-1,1,1),
  (-1,-1,1),
  (1,-1,1),
)

edges = (
  (0,1),
  (0,3),
  (0,4),

  (2,1),
  (2,3),
  (2,6),

  (5,1),
  (5,4),
  (5,6),

  (7,3),
  (7,4),
  (7,6),
)

surfaces = (
  (0,1,2,3),
  (0,1,5,4),
  (0,4,7,3),
  (3,2,6,7),
  (6,5,4,7),  
  (6,2,1,5),  
)

class App:
  ICON_PATH = "./resource/icon.png"
  icon = pg.image.load(ICON_PATH)

  def __init__(self,width,height,title):
    pg.init()
    pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption(title)
    pg.display.set_icon(self.icon)
    self.clock = pg.time.Clock()
    glClearColor(0.1,0.1,0.1,1)
    gluPerspective(45,width/height,0.1,50)
    glTranslatef(0,0,-5)
    self.mainLoop()

  def draw(self):

    glBegin(GL_QUADS)
    for surface in surfaces:
      glColor3f(0.5,0.5,0)
      for vertex in surface:
        glVertex3fv(vertices[vertex])
    glEnd()

    # glBegin(GL_LINES) 
    # glColor3f(0,0,0)
    # for edge in edges:
    #   for vertex in edge:
    #     glVertex3fv(vertices[vertex])
    # glEnd()
    # pass
  
  def mainLoop(self):
    while True:
      for evt in pg.event.get():
        if evt.type == pg.QUIT:
          pg.quit()
      glClear(GL_COLOR_BUFFER_BIT)
      self.draw()
      glRotatef(1,45,90,45)

      self.clock.tick(120)
      pg.time.wait(10)
      pg.display.flip()


if __name__=='__main__':
  app = App(800,600,'Xg Engine Pro 2024')

  