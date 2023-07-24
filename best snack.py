from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snack = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    aim.z = x
    aim.y = y

def insid(head):
    return -200 < head.x < 190 and -200 < head.y <190

def move():
    head = snack[-1].copy()
    head.move(aim)

    if not inside(head) or head in snack:
        square(head.x, head.y, 9, 'red')
        update()
        return
    snack.append()


    if head == food:
        print('snack', len(snack))
        food.x = randrange(-15, 15)*10
        food.y = randrange(-15, 15)*10

    else:
        snack.pop(0)

    clear()

    for body in snack:
        square(body.x, body.y, 9, 'green')


    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)

    hideturtle()
    tracer(False)
    listen()
    onkey(lambda:changes(10, 0), 'right')
    onkey(lambda:changes(-10, 0), 'left')
    onkey(lambda:changes(0, 10), 'up')
    onkey(lambda:changes(0, -10), 'down')


    move()
    done()










        
