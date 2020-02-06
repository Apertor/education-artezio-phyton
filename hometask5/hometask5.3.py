class Observable():

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class X(Observable):

    # def __init__(self, **kwargs):
    #     super(X, self).__init__(**kwargs)

    def __str__(self):
        string = ''
        for attr in self.__dict__:
            if attr[:1] != "_":
                if isinstance(self.__dict__[attr], str):
                    string += "{} = '{}', ".format(attr, self.__dict__[attr])
                else:
                    string += "{} = {}, ".format(attr, self.__dict__[attr])
        string = "X("+string[:len(string)-2]+")"
        return string


x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(x)
print(x.foo)
print(x.name)
print(x._bazz)
