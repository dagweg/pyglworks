import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy.linalg import *
from primitives.primitives import Primitives


class App:
  # ICON_PATH = "./resource/icon.png"
  # icon = pg.image.load(ICON_PATH)
  primitive = Primitives()

  def __init__(self,width,height,title):
    pg.init()
    pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF)
    pg.display.set_caption(title)
    self.clock = pg.time.Clock()
    glClearColor(0.1,0.1,0.1,1)
    gluPerspective(45,width/height,0.1,50)
    glTranslatef(0,0,-5)
    self.mainLoop()

  def draw(self):
    primitive = self.primitive

    glBegin(GL_QUADS)
    for surface in primitive.cube.surfaces:
      for vertex,color in zip(surface,primitive.cube.surfaces_colors):
        glColor3fv(color) 
        glVertex3fv(primitive.cube.vertices[vertex])
    glEnd()

    glBegin(GL_LINES) 
    glColor3f(0.9,0.9,0.9)
    for edge in primitive.cube.edges:
      for vertex in edge:
        glVertex3fv(primitive.cube.vertices[vertex])
    glEnd()
    pass
  
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

  