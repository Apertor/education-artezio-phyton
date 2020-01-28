# 1. Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале [0, Х]. А так же количество таких чисел.

def oddSquare(x):
    interval = range(x)
    list1 = []
    for el in interval:
        if el%2 == 1: list1.append(el**2)
    return list1

x = int(input("#1\nEnter X: "))
print("Square of odd numbers", oddSquare(x))

# 2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’

def divisionOn3el(a, b, c):
    num = 0
    for el in range(a,b):
        if (el!=0)&(el!=a)&(el%c == 0): num=num+1
    return num

a = int(input("\n#2\nEnter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print("Between ", a," and ", b," (not including ", a," and ", b, ") number of numbers divisible by ",c,": ",divisionOn3el(a,b,c))

# 3. Написать функцию вычисления факториала числа

n = input("\n#3\nEnter a number: ")
def fact(n):
    factorial = 1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
           factorial = factorial * i
    return factorial
print("Factorail of ",n , " is : ",fact(n))

# 4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3, только возвращает список).

def myRange(*args):
    start,step=-1,1
    list1=[]

    for i in args:
        if type(i) is not int:
            return "Cannot interpret '{}' as integer!".format(type(i).__name__)

    if len(args)<1:
        return "Range must have at least one argument"

    if len(args)==1:
        stop=(args[0]-step)
        while start<stop:
            start+=(step)
            list1.append(start)
        return list1

    if len(args)==2:
        start=(args[0]-step)
        stop=(args[1]-step)
        while start<stop:
            start+=(step)
            list1.append(start)
        return list1

    if len(args)==3:
        step=args[2]
        if step==0:
            return "Argument 3 should not be zero!"
        start=(args[0]-(step))
        stop=(args[1]-(step))
        if start<stop:
            while start<stop:
                if start<stop:
                    start+=step
                    list1.append(start)
        else:
            while start>stop and step<0:
                start+=step
                list1.append(start)
        return list1
    if len(args)>3:
        return "Expected at most three arguments,got {}".format(len(args))

print("\n#4\nmyRange(3): ",myRange(3))
print("myRange(4,10): ",myRange(4,10))
print("myRange(11,20,2): ",myRange(11,20,2))

# 5. Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с заданным в коде.
# 	В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
# 	Если пароль не совпадает, то печатает в консоль
# 	"Password for user: <Имя пользователя> is incorrect"
# 	"Please try again..."
# 	И снова запрашивает пароль (не завершается).

def authentication(users):
    while True:
        login = input("Enter login: ")
        password = input("Enter password: ")
        if(password == users[login]):
            print("Password for user: <",login,"> is correct")
            break
        else:
            print("Password for user: <", login,"> is incorrect\nPlease try again...")

users = {"user": "Pass1", "dog": "bark"}
print("\n#5\nExisting users: ", users)
authentication(users)