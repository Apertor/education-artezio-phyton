"""hometask 7.2"""
# Напишите параметризованный декоратор для классов,
# который будет считать и выводить время работы методов класса,
# имена которых переданы в параметрах декоратора.

from time import sleep, time


def work_time(function):
    """decorator for function work time determination"""
    def wrapper(*args, **kwargs):
        current_time = time()
        result = function(*args, **kwargs)
        print(f'Время работы {function.__name__} :'
              f' {int((time() - current_time)*1000)} мс.')
        return result
    return wrapper


def time_methods(*methods):
    """decorator for method work time determination"""
    def inner_decorator(specific_class):

        def wrapper(self, *args, **kwargs):
            result = specific_class(self, *args, **kwargs)
            # print(result)

            for method in methods:
                # try:
                if hasattr(specific_class, method):
                    setattr(specific_class, method,
                            work_time(getattr(specific_class, method)))
                # except AttributeError:
                else:
                    print("No method '{}'".format(method))
            return result
        return wrapper
    return inner_decorator


@time_methods('inspect', 'finalize')
class Spam:
    """test class"""

    def __init__(self, some):
        self.some = some

    def inspect(self):
        """make delay"""
        sleep(self.some)

    def foo1(self):
        """return self"""
        return self.some


A = Spam(2)
A.inspect()     # должно вывести сообщение о времени работы
A.foo1()         # ничего не выводить
