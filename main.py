from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys
from Characters import kanye as p
from Resources import handless as h
from Scenes import scene as s


width = 800
height= 600


def init ():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1,0.1,0.1,0.1)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #camara
    glTranslatef(0.0,-1.0,-22)
    glRotatef(10,1,0,0)
    glRotatef(h.angle_x,1,0,0)
    glRotatef(h.angle_y,0,1,0)
    #el oso y el escenario usan Z hacia arriba, esto lo acomoda
    glRotatef(-90,1,0,0)

    p.draw_axes()
    s.draw_escenario()
    p.draw_shapes()
    glutSwapBuffers()

def reshape(w,h):
    global width, height
    width, height = w,h 
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0,float(w)/float(h), 1.0,100.0)
    glMatrixMode(GL_MODELVIEW)



def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(width,height)
    glutCreateWindow(b"Oso Kanye en el escenario")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(h.keyboard)
    glutSpecialFunc(h.special_keys)

    glutMainLoop()

if __name__=="__main__":
    main()
