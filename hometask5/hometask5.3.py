class Observable():

    def __init__(self, **kwargs):
        for attr in list(kwargs.items()):
            self.attr[0] = attr[1]


class X(Observable):

    def __init__(self, **kwargs):
        self.obj = Observable(kwargs)


x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))

print(x)