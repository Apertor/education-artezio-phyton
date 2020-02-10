# 1. Напишите итератор EvenIterator, который позволяет
# получить из списка все элементы, стоящие на чётных индексах.


class EvenIterator:
    """Iterator by even items"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        cur_index = self.index
        self.index += 2
        return self.data[cur_index]


LIST1 = range(11)
MY_ITERATOR = EvenIterator(LIST1)
# print(next(my_iterator))

for i in MY_ITERATOR:
    print(i)
