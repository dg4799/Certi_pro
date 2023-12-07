from collections import namedtuple


list = []
list_value = []
for i in range(1000):
    list.append('key_'+str(i))
    list_value.append(i)
test_nemdtuple = namedtuple("test_nemdtuple", list)
# test = [i for i in list_value]
# print(test)
# t = test_nemdtuple(i for i in list_value)
# print(test_nemdtuple)