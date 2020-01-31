# Пометка: рекомендуемая к прочтению на протяжении всего курса книга - Марк Лутц, "Изучаем Python".
#
# Практические задания к теме "Функции".
#
# Каждое задание должно быть выполнено в отдельном файле.
# Можно пользоваться только встроенными модулями.
# Обязательно соблюдение PEP8. Код должен быть проверен линтерами pylint и flake8.

# 1. Написать несколько функций, которые в качестве единственного аргумента принимают список (или кортеж) целых чисел.
#      - первая функция должна вернуть квадраты элементов коллекции;
#      - вторая функция должна вернуть только элементы на четных позициях;
#      - третья функция возвращает кубы четных элементов на нечетных позициях.


def elem_square(lst):
    list1 = []
    for el in lst:
        list1.append(el ** 2)
    return list1


def pos_even(lst):
    list1 = []
    for el in range(0, len(lst), 2):
        list1.append(lst[el])
    return list1


def elem_even_cube_on_odd_pos(lst):
    list1 = []
    for el in range(1, len(lst), 2):
        odd_el = lst[el]
        if odd_el % 2 == 0:
            list1.append(odd_el**3)
    return list1


lst1 = [el for el in range(3, 10)]
print(lst1)
print(elem_square(lst1))
print(pos_even(lst1))
print(elem_even_cube_on_odd_pos(lst1))
