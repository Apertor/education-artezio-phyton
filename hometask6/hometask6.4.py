# 4.	Написать функцию-генератор cycle
# которая бы возвращала циклический итератор.


###########################################
# 1 solution


def cycle(iterable):
    """cycle('abcd') --> a b c d a b c d ..."""
    saved = []
    for el in iterable:
        yield el
        saved.append(el)
    while saved:
        for el in saved:
            yield el


LIST1 = "abcde"
CI1 = cycle(LIST1)

print("First solution (only function):")
for i in range(8):
    print(next(CI1))


###########################################
# 2 solution with class CycleIterator


class CycleIterator:
    """Cycle iterator"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        cur_index = self.index % len(self.data)
        self.index += 1
        return self.data[cur_index]


def cycle2(obj):
    """Function generator"""
    for it in CycleIterator(obj):
        yield it


LIST2 = range(5)
CI2 = cycle2(LIST2)

print("\nSecond solution (with class):")
for i in range(8):
    print(next(CI2))

# endless loop
# for i in CI2:
#     print(i)
