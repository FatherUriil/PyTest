a = [1, '2', True, None]  # Список с различными типами
a = []  # Empty list
b = list()  # Пустой список

a = (1, 1.1, 22)  # tuple
list(a)  # returns a like list, but stay a a tuple
b = list('abc')

a = [1, 6, 2]
a[0]  # 1
a[1]  # 6
a[2]  # 2
a[3]  # Ошибка
a[-1]  # 2
a[-2]  # 6
a[-3]  # 1
a[-4]  # Error

a = [1, 5, 'women']
a.index('women')  # Возвращает индекс объекта
a = ['g', 3, 5.5, 5.5]
a[0] = 5
a[1] = 'men'
a.append(4)  # добавляет объект в конец списка
a.insert(0, 4)  # adds item into given index
a.insert(['s', 'b'])  # add list into list, may add index
a.extend(['f', 'g'])

del a[0]  # удалить индекс у объекта
del a  # удалить а
a.clear()  # очистить список
a.pop()  # returns last item and remove him
a.remove('aa')  # remove element by value

a = [1, 2, 3]  # 1 dim list
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 2 dim list
b[0][0]  # first: list number second: item number into list

a.count(1)  # returns count of item has into list
a.copy  # copy value of list, if into list has list return reference
a.sort()  # сортировка списка
a.sort(reverse=True)  # sorting list reverse

from copy import deepcopy
b = deepcopy(a)  # copy list recourse