'''Игра виселица'''
from sys import exit
import turtle
from time import sleep
t = turtle.Pen()
import random
from random import randint
t.speed(0)
'''Erase зарисовываем надпись Не верно когда нужно'''
def erase(x,y):
    goto_xy(x,y)
    # t.color("white")
    # t.begin_fill()
    # t.circle(400) Рисует кружок
    # t.end_fill()
    t.color("white")
    t.begin_fill()
    t.begin_poly()
    goto_xy(x+200,y)
    goto_xy(x+200, y+150)
    goto_xy(x,y+150)
    goto_xy(x,y)
    t.end_poly()
    t.end_fill()
'''Переносит курсор черепахи в те координаты куда захотим'''
def goto_xy(x, y):
    t.up()
    t.goto(x, y)
    t.down()
'''Рисуем линии по заданным координатам'''
def draw_line(x1, y1, x2, y2):
    goto_xy(x1,y1)
    t.goto(x2,y2)
'''Функция которая рисует  голову'''
def draw_head(x,y,rad):
    goto_xy(x, y)
    t.circle(rad)
'''Выводим случайное число'''
x = randint(1, 100)
print(x)
'''Считываем координаты'''
with open("test_1.txt") as file:
    koordinates=[]
    for line in file:
        r=list(map(int, line.split(',')))
        koordinates.append(r)
'''Функция которая рисует человека'''
func = [draw_line] * 4 + [draw_head] + [draw_line] * 5

def draw_man(step):
    t.color("blue")
    return func[step](*koordinates[step])
    # if len(koordinates[step]) == 4:
    #     draw_line(*koordinates[step])
    # else:
    #     draw_head(-100, 0,20)
        # goto_xy(-100, 0)
        # t.color("black")
        # t.circle(20)
'''Табличка с вопросом и ответом Верно или Не Верно'''
answer = turtle.textinput('Играть?', 'y/n')
if answer =="n":
    sys.exit()
try_count=-1
question = turtle.textinput('Нужны ли Вам подсказки?','y/n')
'''hints=True if question=="y" else False в одну строчку'''
'''Еще раз в одну сточку hints = question == "y"'''
if question=="y":
    hints=True
else:
    hints=False
while True:
    number = turtle.numinput("Угадайте", 'число', 0, 0, 100)
    if number != x:
        goto_xy(-150, 200)
        t.color("red")
        t.write("НЕ ВЕРНО!", font=("Arial", 28, "normal"))
        try_count+=1
        t.color("black")
        goto_xy(0, -100)
        draw_man(try_count)
        if number>x:
            goto_xy(100,100-try_count*10)
            t.write(f" Загаданное число < {number}")
        else:
            goto_xy(100, 100-try_count*10)
            t.write(f" Загаданное число > {number}")

        if try_count==9:
            erase(-150, 200)
            goto_xy(-20, 230)
            t.color("red")
            t.write("Вы проиграли", font=("Arial", 44, "normal"))
            break
    else:
        erase(-150, 200)
        goto_xy(-150, 100)
        t.color("green")
        t.write("УРА! ВЫ ПОБЕДИЛИ!!!", font=("Arial", 28, "normal"))
        break
sleep(3)