# 3. Написать функцию, которая будет принимать только 4 позиционных аргументы (все аргументы числовые).
#     Функция должна вернуть среднее арифметическое аргументов и самый большой аргумент за все время вызовов этой функции.
#     Пример: foo(1,2,3,4) -> 2.5, 4
#                   foo(-3, -2, 10, 1) -> 1.5, 10
#                   foo(7,8,8,1) -> 6, 10


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(maximum=0)
def foo(a, b, c, d):
    average = (a + b + c + d)/4
    arg = [a, b, c, d]
    m = max(arg)
    if foo.maximum < m:
        foo.maximum = m
    return (average, foo.maximum)


print(foo(1,2,3,4))
print(foo(-3, -2, 10, 1))
print(foo(7,8,8,1))