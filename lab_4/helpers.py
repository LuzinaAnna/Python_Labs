class Mapper:
    """
    Summary:
        Этот клас отображает одно множество значенией в другое.
        Отображение одного множества на другое происходит по необходимости.(Lazy)
    Usage:
        mapped_object = Mapper([1,2,3,4],lambda x : str(x))\n
        result = list(mapped_object)
        result: ['1', '2', '3', '4']
    """

    def __init__(self, collection, function):

        #Если collection является iterable
        if (hasattr(collection, "__iter__")):
            self.iter = iter(collection)
        #Иначе если collection является iterator
        elif (hasattr(collection, "__next__")):
            self.iter = collection
        else:
            #Во всех остальных случаях
            raise AttributeError("collection must be iterable or iterator")

        #Переданный объект функции должен иметь оператор вызова
        if (not hasattr(function, "__call__")):
            raise AttributeError("function must be callable")

        self.function = function

    def __iter__(self):
        #При попытке получить перечислитель объекта, вернется сам объект,
        # т.к. он содержит метод __next__ т.е. является перечислителем
        return self

    def __next__(self):
        return self.function(next(self.iter))


class Filter:
    """
    Summary:
        Этот класс отфильтровывает значения в коллекции.
        Отброс ненужных значений происходит по необходимости.(Lazy)
    Usage:
        filtered_collection = Filter([1,2,3,4],lambda x : x % 2 == 0)\n
        result = list(filtered_collection)
        result: [2,4]
    """

    def __init__(self, collection, predicate):

        #Если collection является iterable
        if (hasattr(collection, "__iter__")):
            self.iter = iter(collection)
        #Иначе если collection является iterator
        elif (hasattr(collection, "__next__")):
            self.iter = collection
        else:
            #Во всех остальных случаях
            raise AttributeError("collection must be iterable or iterator")

        #Переданный объект функции должен иметь оператор вызова
        if (not hasattr(predicate, "__call__")):
            raise AttributeError("predicate must be callable")

        self.function = predicate

    def __iter__(self):
        #При попытке получить перечислитель объекта, вернется сам объект,
        # т.к. он содержит метод __next__ т.е. является перечислителем
        return self

    def __next__(self):

        value = next(self.iter)

        while(not self.function(value)):
            value = next(self.iter)

        return value


def Reduce(collection, initial_value, binary_function):
    """
    Эта функция аккумулирует значения в один результат

    Args:
        collection:         Перечисляемый объект

        initial_value:      Начальное значение аккумулятора

        binary_function:    Бинарная функция, первый аргумент - аккумулятор,
                            второй - очередной аргумент последовательности

    Usage:
        collection = [1,2,3,4,5,6]
        result = Reduce(collection,1,lambda x,y : x*y)
            - В переменной result теперь хранится произведение чисел

    Returns:
        Any: Результат функции зависит от входных параметров
    """
    for value in collection:
        initial_value = binary_function(initial_value, value)

    return initial_value
