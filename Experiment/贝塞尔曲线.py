from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np

# 修改 这个数组的点即可
ControlP = [[-88.0, -40.0, 0.],
            [-10.0, 90.0, 0.],
            [10.0, -90.0, 0.],
            [80.0, 40.0, 0.], [20, 20, 0.]]


def GetCnk(n: int, c: list):
    for k in range(n+1):
        c[k] = 1
        for i in range(n, k, -1):
            c[k] = c[k] * i
        for i in range(n-k, 1, -1):
            c[k] = c[k] / i

# 计算Bezier曲线上点的坐标


def GetPointPr(c: list,  t: float, Pt: dict, ControlN: int, ControlP: int):
    k = ControlN - 1
    n = ControlN-1
    Pt['x'] = 0.0
    Pt['y'] = 0.0
    Pt['z'] = 0.0
    for k in range(ControlN):
        Bernstein = c[k] * pow(t, k) * pow(1 - t, n - k)
        Pt['x'] += ControlP[k][0] * Bernstein
        Pt['y'] += ControlP[k][1] * Bernstein
        Pt['z'] += ControlP[k][2] * Bernstein


# 根据控制点, 求曲线上的m个点
def initial():
    glClearColor(1.0, 1.0, 1.0, 0.0)


def BezierCurve(m: int, ControlN: int,  ControlP: list):
    C = [0]*ControlN
    CurvePt = {
        'x': 0,
        'y': 0,
        'z': 0
    }
    GetCnk(ControlN - 1, C)
    glBegin(GL_POINTS)
    for i in range(m+1):
        GetPointPr(C, i / m, CurvePt, ControlN, ControlP)
        glVertex2f(CurvePt['x'], CurvePt['y'])
    glEnd()


def Reshape(newwidth,  newHeight):
    glViewport(0, 0, newwidth, newHeight)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)


def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    ControlN = len(ControlP)
    m = 500
    # 指定有4个控制点, 生成的Bezier曲线由500个点组成
    # 控制点坐标
    # 设置当前绘制点大小
    glPointSize(2)
    glColor3f(0.0, 0.0, 0.0)
    # 绘制控制多边形
    BezierCurve(m, ControlN, ControlP)
    # 绘制Bezier曲线
    glBegin(GL_LINE_STRIP)
    for i in range(len(ControlP)):
        glVertex3f(ControlP[i][0], ControlP[i][1], ControlP[i][2])
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Bezier curve")
    initial()
    glutDisplayFunc(Display)
    glutReshapeFunc(Reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
