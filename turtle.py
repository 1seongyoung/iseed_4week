import turtle
import random
import math
from tkinter.simpledialog import *

swidth, sheight = 500, 500
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)
turtle.title('거북이로 나선형 문자열 쓰기')
turtle.shape('turtle')

inStr = askstring('문자열 입력', '거북이가 쓸 문자열을 입력:')
radius = 200
angle = 0

turtle.goto(swidth / 2, sheight / 2 - radius)

for ch in inStr:
    radian = math.radians(angle)
    turtle.pencolor(random.random(), random.random(), random.random())

    tx = radius * math.cos(radian)
    ty = radius * math.sin(radian)
    turtle.goto((swidth / 2) + tx, (sheight / 2) + ty)
    turtle.write(ch, font=('맑은 고딕', 20, 'bold'))
    
    radius -= 10 
    angle += 20 

turtle.done()
