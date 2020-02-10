# 3. Есть два списка разной длины, в одном ключи, в другом значения. Составить словарь.
# Для ключей, для которых нет значений использовать None в качестве значения.
# Значения, для которых нет ключей игнорировать.


class SafeList(list):
    """Add method get to list with None by default"""

    def get(self, index, default=None):
        """Method get by index for list with None by default"""
        try:
            return self.__getitem__(index)
        except IndexError:
            return default


LIST1 = range(5)
LIST2 = "abc"

# dic = dict(zip(list1, list2))
# dic = {k: v for k, v in zip(list1, list2)}
DIC = {k: SafeList(LIST2).get(i) for i, k in enumerate(LIST1)}
print(DIC)
