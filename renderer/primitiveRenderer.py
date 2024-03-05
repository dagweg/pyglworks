import OpenGL.GL as gl

class Primitive3D:
  def __init__(self):
    pass

  @staticmethod
  def render(primitive, color=None, wireframe=False, wireColor=(0,0,0)):
    gl.glBegin(gl.GL_QUADS)
    for surface in primitive.surfaces:
      for vertex,surf_color in zip(surface,primitive.surfaces_colors):
        gl.glColor3fv(color if color else surf_color) 
        gl.glVertex3fv(primitive.vertices[vertex])
    gl.glEnd()
    
    if wireframe:
      gl.glBegin(gl.GL_LINES) 
      gl.glColor3fv(wireColor)
      for edge in primitive.edges:
        for vertex in edge:
          gl.glVertex3fv(primitive.vertices[vertex])
      gl.glEnd()



    