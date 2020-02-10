# 2.	Написать генератор списка для получения
# списка всех публичных атрибутов объекта


class MyClass:
    """class with two public attributes"""
    attr1 = ''
    attr2 = 0

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


OBJ = MyClass("a", 1)
A = [i for i in OBJ.__dict__ if i[:1] != "_"]
print(A)
