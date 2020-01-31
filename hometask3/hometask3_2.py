# 2. Написать функцию, которая принимает произвольное количество любых аргументов.
#     Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
#     Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
#     Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
#     Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
#     При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.


def inside(el, iSum, prod):
    nsum = iSum
    nprod = prod
    if isinstance(el, list) | isinstance(el, tuple):
        for i in el:
            res = inside(i, nsum, nprod)
            nsum = res[0]
            nprod = res[1]
    else:
        if el != 0:
            nsum += el
            nprod *= el
    return [nsum, nprod]


def func(*args, **kwargs):
    rSum = 0
    prod = 1
    arr = list(args)+list(kwargs.values())
    print("Input arguments", arr)
    for el in arr:
        if isinstance(el, type(None)):
            print("Not supported arguments")
            return None
        else:
            result = inside(el, rSum, prod)
            rSum = result[0]
            prod = result[1]
    return result


test1 = func(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
print("Result", test1, "\n")

a = [1, 2, 3]
test2 = func(a.append(a), 1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
print("Result", test2)