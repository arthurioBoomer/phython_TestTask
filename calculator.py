def main(string):
    if string == "":
        print("Вы ничего не ввели")
        quit()
    elif string.count(" ") <= 1:
        print("Не соответствует выражению в формате \"a + b\", \"a - b\", \"a * b\" или \"a / b\"")
        quit()
    elif string.count(" ") > 2:
        print("Введите математическое выражение из 2 числа и 1 оператор между ними, записывается через пробел")
        quit()
    else:
        vvod = string.split(" ")

    try:
        a1 = float(vvod[0])
    except ValueError:
        print("Математическое выражение написано неверно, \"a\" не является числом")
        quit()
    if a1 % 1 != 0:
        print("Калькулятор работает только с целыми числами, число \"a\" - иррациональное")
        quit()

    try:
        b1 = float(vvod[2])
    except ValueError:
        print("Математическое выражение написано неверно, \"b\" не является числом")
        quit()
    if b1 % 1 != 0:
        print("Калькулятор работает только с целыми числами, число \"b\" - иррациональное")
        quit()

    a = int(a1)
    b = int(b1)

    operator = vvod[1]

    if a < -10:
        print("Число \"a\" не соответствует требуемому диапозону значений, ваше число меньше -10")
        quit()
    elif a > 10:
        print("Число \"a\" не соответствует требуемому диапозону значений, ваше число больше 10")
        quit()

    if b < -10:
        print("Число \"b\" не соответствует требуемому диапозону значений, ваше число меньше -10")
        quit()
    elif b > 10:
        print("Число \"b\" не соответствует требуемому диапозону значений, ваше число больше 10")
        quit()

    if operator == "+":
        print("Результат сложения - ", summ(a, b))
    elif operator == "-":
        print("Результат умножения - ", mult(a, b))
    elif operator == "*":
        print("Результат умножения - ", mult(a, b))
    elif operator == "/":
        print("Результат деления - ", dev(a, b))
    else:
        print("Математическое выражение написано неверно, нет нужного оператора \"+\", \"-\", \"*\" или \"/\"")
        quit()


def summ(a, b):
    result = a + b
    return result

def subt(a, b):
    result = a - b
    return result

def mult(a, b):
    result = a * b
    return result

def dev(a, b):
    try:
        result = a // b
        return result
    except ZeroDivisionError:
        print("В математике нельзя делить на ноль.")


i = 1
while i < 2:
    print("Введите арифметическую операцию с двумя числами в формате \"a + b\", \"a - b\", \"a * b\" или \"a / b\"")
    main(string=str(input("для вычисления калькулятором(использовать можно только целые числа от -10 до 10)\n")))
