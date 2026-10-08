from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys


angle_x = 0
angle_y = 0

def keyboard(key,x,y):
    global angle_x, angle_y

    if key == b'\x1b' :
        sys.exit()

def special_keys(key,x,y):
    global angle_x, angle_y
    if key == GLUT_KEY_RIGHT:
        angle_y +=5
    elif key ==GLUT_KEY_LEFT:
        angle_y -=5
    elif key ==GLUT_KEY_UP:
        angle_x -=5
    elif key ==GLUT_KEY_DOWN:
        angle_x +=5
    glutPostRedisplay()