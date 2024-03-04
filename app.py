import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

def draw():

  pass

def reshape(w,h):
  gl.glViewport(0,0,w,h)

def main():
  width = 640
  height = 480

  glut.glutInit()
  if glut.INITIALIZED:
    glut.glutDisplayFunc(draw)
    glut.glutReshapeFunc(reshape)
    glut.glutInitWindowSize(width,height)
    glut.glutCreateWindow("Unity 2024.0.1f1")
    glut.glutMainLoop()

if __name__ == '__main__':
  main()