"""hometask 7.4"""
# Написать декоратор, который будет проверять тип аргументов
# при вызове функции согласно аннотации функции.
# Декорирование функции без аннотации или с неполной аннотацией
# (когда аннотированы не все аргументы) должно рейзить ошибку.
# В случае несовпадения переданных во время вызова функции аргументов
# с типами аргументов в аннотации - выводить сообщение.

def get_args_dict(function):
    """decorator for argument type check"""
    def wrapper(*args, **kwargs):
        args_name = function.__code__.co_varnames[:function.__code__.co_argcount]
        # print(kwargs.items(kwargs))
        args_dict = dict(zip(args_name, args))
        ann = function.__annotations__
        # print(args_dict)
        # print(ann)

        try:
            for arg in args_dict:
                if not isinstance(args_dict[arg], ann[arg]):
                    print(f"Value '{args_dict[arg]}' of variable '{arg}'"
                          f" does not match the type {ann[arg]}"
                          f" specified in the annotation")
        except KeyError as error:
            print(f"No annotation assigned to variable {error}")
            raise
        return function(*args)

    return wrapper

# def get_args_dict(fn, *args, **kwargs):
#     args_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
#     return {**dict(zip(args_names, args)), **kwargs}


@get_args_dict
def repeater(s: str, n: int, d) -> str:
    """test function"""
    print(d)
    return s * n

repeater(2, 3, 'hi')
