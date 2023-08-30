#coding = utf-8

from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.6, -0.6)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.6, -0.6)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.6)
    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"PyOpenGL Simple Triangle")
    glutDisplayFunc(display)
    glutMainLoop()
