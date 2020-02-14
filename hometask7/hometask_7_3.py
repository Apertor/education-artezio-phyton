"""hometask 7.3"""
# Каррирование.
# Преобразовать вызов функции с конечным количеством позиционных аргументов
# f(a, b, c, d) в вызов вида f(a)(b)(c)(d), используя декоратор.


def carry(func, arg_count=None):
    """currying decorator"""

    # first decorator call
    if arg_count is None:
        arg_count = func.__code__.co_argcount
        # print("initial arg count ", arg_count)

    # a - first argument in curring function
    # step 1: a = 1
    # step 2: a = 2
    # step 3: a = 3
    def wrapper(*a):
        # print(f"step {carry.count_ew}: a = {a}")

        # for last argument call in currying function
        if len(a) == arg_count:
            return func(*a)

        # b - rest function arguments (without a)  in curring function
        # without recursion
        # step 1: b = (2, 3)
        # step 2: b = (3, )
        # step 3: no
        def inside_wrapper(*b):
            # print(f"step {carry.count_iw}: a = {a}, b = {b}")
            # carry.count_iw += 1
            result = func(*(a + b))
            return result

        # carry.count_ew += 1

        # recursion
        # step 1: func(3)
        # step 2: func(2, 3)
        # step 3: func(1, 2, 3)
        return carry(inside_wrapper, arg_count - len(a))
    return wrapper

# carry.count_iw = 1
# carry.count_ew = 1

@carry
def foo(a, b, c):
    """test function"""
    return a + b * c

print(foo(1)(2)(3))
