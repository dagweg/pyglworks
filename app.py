import pygame as pg
from pygame.locals import *
from OpenGL.GL import *

class App:
  ICON_PATH = "./resource/icon.png"
  MODEL_PATH = './resource/cube.obj'
  icon = pg.image.load(ICON_PATH)

  def __init__(self,width,height,title):
    pg.init()
    self.screen = pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption(title)
    pg.display.set_icon(self.icon)
    self.clock = pg.time.Clock()

    self.cube = pg.image.load(self.MODEL_PATH).convert()


    glClearColor(1,1,1,1)
    self.mainLoop()
  
  def mainLoop(self):
    running = True
    while running:
      for evt in pg.event.get():
        if evt.type == pg.QUIT:
          running = False
      

      glClear(GL_COLOR_BUFFER_BIT)
      pg.display.flip()

      self.screen.blit(self.cube,(0,0))

      self.clock.tick(60)
    self.quit()

  def quit(self):
    pg.quit()

if __name__=='__main__':
  app = App(640,480,'Xg Engine Pro 2024')

  