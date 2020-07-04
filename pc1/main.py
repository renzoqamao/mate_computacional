import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices= (
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1 ,0),

    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, 1, 1),
    )
edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),

    (0,4),
    (1,5),
    (2,6),
    (3,7),

    (4,5),
    (5,6),
    (6,7),
    (7,4)
    )

def Cube():
    glColor3f(1.0, 0.4, 0.8)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
def ejes():
    glPushMatrix()
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(3.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 3.0)
    glEnd()
    glPopMatrix()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslate(0,0,-5)
    rota=0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    if rota< 360:
                        rota = rota + 30
                elif event.key == pygame.K_DOWN:
                    if rota > -360:
                        rota = rota - 30
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        ejes()
        glPushMatrix()
        glRotatef(rota, 1, 1, 1)
        Cube()
        glPopMatrix()
        pygame.display.flip()
        #pygame.time.wait(1)


main()
