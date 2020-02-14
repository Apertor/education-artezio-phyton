"""hometask 7.1"""
# Напишите параметризованный декоратор, который считает
# и выводит при каждом вызове среднее время работы функции
# за n последних вызовов. Время выводить в миллисекундах.

#   Пример использования:
#
#   @average_time(n=2)
#   def foo(a):
#       sleep(a)
#       return a
#
#   foo(3) # вернет 3 и выведет сообщение "Среднее время работы: 3000 мс."
#   foo(7) # вернет 7 и выведет сообщение "Среднее время работы: 5000 мс."
#   foo(1) # вернет 1 и выведет сообщение "Среднее время работы: 4000 мс."

from time import sleep, time

def average_time(n=1):
    """function average time calculation in defined number of calls"""
    def inner_decorator(function):
        wtime = []
        def wrapper(*args, **kwargs):
            # nonlocal wtime
            current_time = time()
            result = function(*args, **kwargs)
            work_time = 0
            num = 0
            start = 0
            wtime.append(time()-current_time)
            at_len = len(wtime)
            if at_len > n:
                start = at_len-n
            for curr_time in wtime[start:]:
                work_time += curr_time
                num += 1
            print(f'Среднее время работы: {int(work_time*1000/num)} мс.')
            return result
        return wrapper
    return inner_decorator

@average_time(n=2)
def foo(a):
    """test function"""
    sleep(a)
    return a

print(foo(3))
print(foo(7))
print(foo(1))
