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
        args_kwargs_name = function.__code__.co_varnames[:function.__code__.co_argcount]
        ann = function.__annotations__
        args_kwargs_dict = dict(zip(args_kwargs_name, list(args)
                                    + [i[1] for i in kwargs.items()]))

        # print("args and kwargs names: ", args_kwargs_name)
        # print("annotation: ", ann)
        # print("args and kwargs values: ", args_kwargs_dict)

        try:
            for arg in args_kwargs_dict:
                if not isinstance(args_kwargs_dict[arg], ann[arg]):
                    print(f"Value '{args_kwargs_dict[arg]}' of variable '{arg}'"
                          f" does not match the type {ann[arg]}"
                          f" specified in the annotation")
        except KeyError as error:
            print(f"No annotation assigned to variable {error}")
            raise
        return function(*args, **kwargs)

    return wrapper

# def get_args_dict(fn, *args, **kwargs):
#     args_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
#     return {**dict(zip(args_names, args)), **kwargs}


@get_args_dict
def repeater(s: str, n: int, d: str = 'j', v: int = 2) -> str:
    """test function"""
    return [s * n, d, v]


print("\n", repeater(2, 3, 1, v="0"))
