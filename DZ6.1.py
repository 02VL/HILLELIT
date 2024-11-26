# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string
a = input("введіть діапазон букв через дефіс: ")
s = str(string.ascii_letters[int(string.ascii_letters.find(a[0])):int(string.ascii_letters.find(a[-1]))+1])
print(s)
