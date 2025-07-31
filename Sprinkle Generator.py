from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

points = []
speed = 1
isFrozen = False
bg=True


def draw_points(x, y, color):
    glPointSize(5)
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def generate_random_points(x, y):
    for i in range(10):
        color = generate_random_color()
        spd = generate_random_speed()
        direction_x = generate_random_direction()
        direction_y = generate_random_direction()
        points.append({'x': x, 'y': y, 'color': color, 'black': [0,0,0], 'speed': spd, 'dx': direction_x, 'dy': direction_y})

def generate_random_color():
    return [random.random(), random.random(), random.random()]

def generate_random_speed():
      return random.uniform(0.1, 0.2) * speed

def generate_random_direction():
    return random.choice([-1, 1])


def mouseClickListener(button, state, x, y):
    global points,bg
    if button == GLUT_RIGHT_BUTTON :
        generate_random_points(x, y)

    if button == GLUT_LEFT_BUTTON :
        if bg==True:
            bg=False
        else:
            bg=True
        

def specialKeyListener(key, x, y):
    global speed, isFrozen,bg
    if key == GLUT_KEY_UP:
        speed += 0.1
    if key == GLUT_KEY_DOWN and speed :
        speed -= 0.1

def animate():
    global points,space
    if not isFrozen:
        for point in points:
            
            point['x'] += point['dx'] * point['speed']
            point['y'] += point['dy'] * point['speed']
    glutPostRedisplay()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    iterate()
    global points,bg


    if bg==True:
        for point in points:
            draw_points(point['x'], point['y'], point['color'])
    else:
        for point in points:
            draw_points(point['x'], point['y'], point['black'])
    

    glutSwapBuffers()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Random Points")

glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseClickListener)

glutMainLoop()
