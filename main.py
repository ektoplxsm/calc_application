from tkinter import *
import math

root = Tk()  # основа
root.geometry("400x400")  # размер приложения
root.title("Калькулятор")  # название приложения
root.config(background="purple")  # цвет фона приложения

expression = ""

result = StringVar()
expression_field = Entry(textvariable=result)  # окно ввода текста
expression_field.grid(columnspan=5, ipadx=100)  # размер окна


def press_num(num):  # функция нажатия на кнопки
    global expression  # объявление переменной expression глобальной
    expression += str(num)  # добавление данных в переменную expression
    result.set(expression)  # передача значения в поле ввода


def calculation():
    try:
        global expression
        total = str(eval(
            expression))  # Решение уравнения, eval решает само уравнение.
        result.set(total)
        expression = total
    except:
        result.set("error")  # Если в условии try произошла ошибка, вывести error.
        expression = ""


def sqrt_exp():  # функция корня
    global expression
    total = str(math.sqrt(eval(expression)))
    result.set(total)
    expression = total


def square_exp():  # функция квадрата
    global expression
    total = str((eval(expression) * (eval(expression))))
    result.set(total)
    expression = total


def reset():  # функция сброса
    global expression
    total = ""
    result.set(total)
    expression = total


button1 = Button(text='1', height=1, width=7, command=lambda: press_num(1))  # Кнопка "1"
button1.grid(row=2, column=0)

button2 = Button(text='2', height=1, width=7, command=lambda: press_num(2))  # Кнопка "2"
button2.grid(row=2, column=1)

button3 = Button(text='3', height=1, width=7, command=lambda: press_num(3))  # Кнопка "3"
button3.grid(row=2, column=2)

button4 = Button(text='4', height=1, width=7, command=lambda: press_num(4))  # Кнопка "4"
button4.grid(row=3, column=0)

button5 = Button(text='5', height=1, width=7, command=lambda: press_num(5))  # Кнопка "5"
button5.grid(row=3, column=1)

button6 = Button(text='6', height=1, width=7, command=lambda: press_num(6))  # Кнопка "6"
button6.grid(row=3, column=2)

button7 = Button(text='7', height=1, width=7, command=lambda: press_num(7))  # Кнопка "7"
button7.grid(row=4, column=0)

button8 = Button(text='8', height=1, width=7, command=lambda: press_num(8))  # Кнопка "8"
button8.grid(row=4, column=1)

button9 = Button(text='9', height=1, width=7, command=lambda: press_num(9))  # Кнопка "9"
button9.grid(row=4, column=2)

addition = Button(text='+', height=1, width=7, command=lambda: press_num("+"))  # Кнопка "+"
addition.grid(row=5, column=0)

button0 = Button(text='0', height=1, width=7, command=lambda: press_num(0))  # Кнопка "0"
button0.grid(row=5, column=1)

subtraction = Button(text='-', height=1, width=7, command=lambda: press_num("-"))  # Кнопка "-"
subtraction.grid(row=5, column=2)

equals = Button(text='=', height=1, width=7, command=calculation)  # Кнопка "="
equals.grid(row=6, column=1)

multiplication = Button(text='*', height=1, width=7, command=lambda: press_num("*"))  # Кнопка "*"
multiplication.grid(row=6, column=2)

division = Button(text='/', height=1, width=7, command=lambda: press_num("/"))  # Кнопка "/"
division.grid(row=6, column=0)

sqrt = Button(text='sqrt', height=1, width=7, command=sqrt_exp)  # Кнопка "sqrt", корень
sqrt.grid(row=7, column=1)

square = Button(text='**', height=1, width=7, command=square_exp)  # Кнопка "**", квадрат
square.grid(row=7, column=0)

reset = Button(text='C', height=1, width=7, command=reset)  # Кнопка "C", сброс
reset.grid(row=7, column=2)

dot = Button(text='.', height=1, width=7, command=lambda: press_num("."))  # Кнопка ".", для плавающей запятой
dot.grid(row=8, column=0)

root.mainloop()