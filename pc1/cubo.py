from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
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

#teclas
ESCAPE = '\033'
a ='\141'
d = '\144'
w = '\167'
s = '\163'
f = '\146'
r = '\162'
rota = 0

#dibuja los ejes
def ejes():
    glPushMatrix()
    glBegin(GL_LINES)

    glColor3f(1.0, 0.5, 0.7)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(3.0, 0.0, 0.0)

    glColor3f(0.5, 1.0, 0.7)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 3.0, 0.0)

    glColor3f(0.7, 0.5, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 3.0)
    glEnd()
    glPopMatrix()

#dibuja el cubo
def Cube():
    global rota
    glPushMatrix()
    glColor3f(1.0, 0.4, 0.8)
    glRotatef(rota,1.0,1.0,1.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    glPopMatrix()

#renderizado
#def initRendering():
    #glEnable(GL_DEPTH_TEST);
    #glEnable(GL_LIGHTING);
    #glEnable(GL_LIGHT0);      # luz .

#keyboardFunc
def keyboard(key, x, y):
    global rota, w, s, ESCAPE
    if key == w:
        if rota < 360:
            rota = rota + 30
    elif key == s:
        if rota > -360:
            rota = rota - 30
    elif key == ESCAPE:
        sys.exit()
    # Esta funcion indica a la GLUT que es necesario redibujar la ventana
    glutPostRedisplay()
#keyboardFunc
def KeyPressed(*args):
    global rota, w, s, ESCAPE
    if args[0] == w:
        if rota < 360:
            rota = rota + 30
    elif args[0] == s:
        if rota > -360:
            rota = rota - 30
    elif args[0] == ESCAPE:
        sys.exit()
    # Esta funcion indica a la GLUT que es necesario redibujar la ventana
    glutPostRedisplay()

"""def specialFunc(key, x, y ):
    #case GLUT_KEY_UP: // modifica la posicion de la luz hacia arriba
    #case GLUT_KEY_DOWN: // modifica la posicion de la luz hacia abajo
    #case GLUT_KEY_LEFT: // modifica la posicion de la luz hacia la izquierda
    #case GLUT_KEY_RIGHT:// modifica la posicion de la luz hacia la derecha
    #glutPostRedisplay() """

#camara
def handler( width ,  height):
    if width > height:
        width = height
    else:
        height=width

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50.0, height/width, 0.1 , 50.0)
    #gluLookAt define la transformacion sobre la vista inicial.
	#tiene 9 parametros: los primeros tres representan la
	#distancia en x, y, z de los ojos del observador
	#los siguientes tres, las coordenadas x,y, z del punto de referencia aobservar
	# y los ultimos tres, la direccion del upVector
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity()
    gluLookAt(2.5, 5.0, 2.5, 0.0, 0.0, 0.0,  0.0, 1.0, 0.0);

#dibuja
def draw():
    ejes()
    Cube()

#dibuja la escena
def drawScene():
    #limpia la pantalla y pinta el fondo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glMatrixMode( GL_MODELVIEW );
    #glLoadIdentity();
    draw()
    #glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    #esquema decolor RGB
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )
    #posicion de la ventana al iniciar
    glutInitWindowPosition( 60, 60 )
    #tamanio de la ventana
    glutInitWindowSize( 800, 800 )
    #nombre
    glutCreateWindow("CUBO");
    #renderizado
    #initRendering();
    #funciones de teclado
    glutKeyboardFunc(keyboard)
    #funciones de teclado
    #glutSpecialFunc(specialFunc)
    #modifica la perspectiva
    glutReshapeFunc(handler)
    #dibuja
    glutDisplayFunc( drawScene )
    #redibuja
    glutMainLoop()

main()
