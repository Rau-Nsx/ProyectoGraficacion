from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
 
# El oso (escala 0.375 y centrado) tiene los pies en z = -2.78
PISO = -2.78
 
 
def draw_escenario():
    quad=gluNewQuadric()
    gluQuadricDrawStyle(quad,GLU_FILL)
 
    #base del escenario
    glPushMatrix()
    glTranslatef(0,-1,PISO-0.86)
    glScalef(16,10,1.68)
    glColor3f(0.30,0.20,0.12)
    glutSolidCube(1)
    glPopMatrix()
    #piso de madera
    glPushMatrix()
    glTranslatef(0,-1,PISO-0.01)
    glScalef(16,10,0.02)
    glColor3f(0.42,0.27,0.15)
    glutSolidCube(1)
    glPopMatrix()
    #tablones
    for i in range(20):
        glPushMatrix()
        glTranslatef(0,-5.75+i*0.5,PISO+0.005)
        glScalef(16,0.03,0.01)
        glColor3f(0.25,0.15,0.08)
        glutSolidCube(1)
        glPopMatrix()
    #escalon frontal
    glPushMatrix()
    glTranslatef(0,-6.6,PISO-1.2)
    glScalef(14,1.2,0.9)
    glColor3f(0.35,0.22,0.13)
    glutSolidCube(1)
    glPopMatrix()
 
    #pared de ladrillo
    glPushMatrix()
    glTranslatef(0,4.2,1.76)
    glScalef(16,0.4,12.48)
    glColor3f(0.70,0.45,0.42)
    glutSolidCube(1)
    glPopMatrix()
    #juntas de ladrillo
    for i in range(26):
        glPushMatrix()
        glTranslatef(0,3.99,PISO+0.2+i*0.4)
        glScalef(16,0.02,0.03)
        glColor3f(0.55,0.33,0.32)
        glutSolidCube(1)
        glPopMatrix()
 
    #franja de cuadros
    for i in range(30):
        for j in range(2):
            glPushMatrix()
            glTranslatef(-7.25+i*0.5,3.95,-0.2+j*0.5)
            glScalef(0.5,0.1,0.5)
            if (i+j)%2==0:
                glColor3f(0.05,0.05,0.05)
            else:
                glColor3f(0.95,0.8,0.9)
            glutSolidCube(1)
            glPopMatrix()
 
    #bocinas
    for s in (1,-1):
        x=s*6.0
        #cuerpo
        glPushMatrix()
        glTranslatef(x,3.0,-0.98)
        glScalef(1.6,1.4,3.6)
        glColor3f(0.22,0.17,0.22)
        glutSolidCube(1)
        glPopMatrix()
        for z in (-1.9,-0.4):
            #woofer
            glPushMatrix()
            glTranslatef(x,2.3,z)
            glRotatef(90,1,0,0)
            glColor3f(0.12,0.09,0.12)
            gluCylinder(quad,0.55,0.55,0.06,24,1)
            glTranslatef(0,0,0.06)
            gluDisk(quad,0,0.55,24,1)
            glPopMatrix()
            #centro del woofer
            glPushMatrix()
            glTranslatef(x,2.24,z)
            glScalef(1,0.5,1)
            glColor3f(0.30,0.20,0.30)
            glutSolidSphere(0.22,16,16)
            glPopMatrix()
 
    #cortinas con estrellas
    for s in (1,-1):
        cx=s*8.2
        cy=1.5
        #cortina
        glPushMatrix()
        glTranslatef(cx,cy,PISO-1.7)
        glColor3f(0.25,0.15,0.40)
        gluCylinder(quad,1.3,1.3,12.48,32,1)
        glTranslatef(0,0,12.48)
        gluDisk(quad,0,1.3,32,1)
        glPopMatrix()
        #estrellas
        for k in range(12):
            for a in range(5):
                ang=math.radians(200+a*35+(k%2)*17)
                glPushMatrix()
                glTranslatef(cx+1.31*math.cos(ang),cy+1.31*math.sin(ang),PISO+0.3+k*0.9)
                glColor3f(0.60,0.50,0.30)
                glutSolidSphere(0.09,6,6)
                glPopMatrix()
 
    #nubes colgantes
    circulos=[(-1.1,-0.2,0.35),(-0.6,-0.5,0.5),(-0.7,0.35,0.3),(0.0,0.1,0.65),
              (0.15,-0.7,0.5),(0.8,-0.1,0.6),(1.1,-0.85,0.3),(0.95,0.55,0.4)]
    for cx in (-5.0,-0.8,5.4):
        nz=5.0
        #cuerdas
        for dx in (-0.7,0.7):
            glPushMatrix()
            glTranslatef(cx+dx,3.85,6.85)
            glScalef(0.06,0.06,2.3)
            glColor3f(0.05,0.05,0.05)
            glutSolidCube(1)
            glPopMatrix()
        for i in range(len(circulos)):
            dx,dz,r=circulos[i]
            yb=3.75-0.03*i
            #contorno oscuro
            glPushMatrix()
            glTranslatef(cx+dx,yb,nz+dz)
            glRotatef(90,1,0,0)
            glColor3f(0.20,0.18,0.22)
            gluCylinder(quad,r+0.07,r+0.07,0.1,24,1)
            glTranslatef(0,0,0.1)
            gluDisk(quad,0,r+0.07,24,1)
            glPopMatrix()
            #circulo claro
            glPushMatrix()
            glTranslatef(cx+dx,yb-0.05,nz+dz)
            glRotatef(90,1,0,0)
            glColor3f(0.85,0.65,0.82)
            gluCylinder(quad,r,r,0.07,24,1)
            glTranslatef(0,0,0.07)
            gluDisk(quad,0,r,24,1)
            glPopMatrix()
 
    #sol
    #cuerda del sol
    glPushMatrix()
    glTranslatef(2.5,3.9,7.35)
    glScalef(0.06,0.06,1.3)
    glColor3f(0.05,0.05,0.05)
    glutSolidCube(1)
    glPopMatrix()
    #aro naranja
    glPushMatrix()
    glTranslatef(2.5,3.8,5.2)
    glRotatef(90,1,0,0)
    glColor3f(0.95,0.40,0.05)
    gluCylinder(quad,1.0,1.0,0.1,32,1)
    glTranslatef(0,0,0.1)
    gluDisk(quad,0,1.0,32,1)
    glPopMatrix()
    #centro del sol
    glPushMatrix()
    glTranslatef(2.5,3.78,5.2)
    glRotatef(90,1,0,0)
    glColor3f(0.80,0.55,0.40)
    gluCylinder(quad,0.85,0.85,0.1,32,1)
    glTranslatef(0,0,0.1)
    gluDisk(quad,0,0.85,32,1)
    glPopMatrix()
    #rayos
    for k in range(12):
        glPushMatrix()
        glTranslatef(2.5,3.8,5.2)
        glRotatef(k*30,0,1,0)
        glTranslatef(0,0,0.95)
        glScalef(1,0.15,1)
        glColor3f(0.95,0.40,0.05)
        glutSolidCone(0.25,0.55,12,1)
        glPopMatrix()