import string
def add_one(some_list):
    str1 = "".join(map(str, some_list))
    a = int(str1)+1
    a1 = str(a)
    lst1 = []
    for i in a1:
        lst1.append(int(i))
    return lst1



assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
print("ОК")
