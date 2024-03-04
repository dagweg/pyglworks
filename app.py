import pygame as pg
from OpenGL.GL import *

class App:
  ICON_PATH = "./resource/icon.png"
  icon = pg.image.load(ICON_PATH)

  def __init__(self,width,height,title):
    pg.init()
    pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption(title)
    print(self.icon)
    pg.display.set_icon(self.icon)
    self.clock = pg.time.Clock()
    #initialize opengl
    glClearColor(0.1,0.1,0.1,1)
    self.mainLoop()
  
  def mainLoop(self):
    running = True
    while running:
      for evt in pg.event.get():
        if evt.type == pg.QUIT:
          running = False
        
      glClear(GL_COLOR_BUFFER_BIT)
      self.clock.tick(60)
    self.quit()

  def quit(self):
    pg.quit()

if __name__=='__main__':
  app = App(500,500,'Unity Destroyer 2024')

  