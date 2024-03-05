import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from pywavefront import Wavefront
import numpy as np
from collections import deque
from numpy.linalg import *
import random

class App:
  ICON_PATH = "./resource/icon.png"
  MODEL_PATH = './resource/cube.obj'
  icon = pg.image.load(ICON_PATH)

  def __init__(self,width,height,title):
    pg.init()
    pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption(title)
    pg.display.set_icon(self.icon)
    self.clock = pg.time.Clock()

    glClearColor(0.8,0.8,0.8,1)
    self.mainLoop()

  def draw(self):
    r = random.random()
    g = random.random()
    b = random.random()
    glBegin(GL_TRIANGLES)
    glColor3f(r,g,b)
    glVertex3f(-0.5,0,0)
    glVertex3f(0.5,0,0)
    glVertex3f(0,0.5,0)
    glEnd()
    pass
  
  def mainLoop(self):
    running = True
    while running:
      for evt in pg.event.get():
        if evt.type == pg.QUIT:
          running = False
      glClear(GL_COLOR_BUFFER_BIT)
      self.draw()
      pg.display.flip()
      self.clock.tick(5)
    self.quit()

  

  def quit(self):
    q=deque()
    pg.quit()

if __name__=='__main__':
  app = App(640,480,'Xg Engine Pro 2024')

  