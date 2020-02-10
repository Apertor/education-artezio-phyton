# 5.	Написать функцию-генератор chain,
# которая последовательно итерирует
# переданные объекты (произвольное количество)


def chain(*iterables):
    """chain('abc', 'def') --> a b c d e f"""
    for it in iterables:
        for el in it:
            yield el


LIST1 = range(5)
LIST2 = "abcd"
CI = chain(LIST1, LIST2)

for i in CI:
    print(i)