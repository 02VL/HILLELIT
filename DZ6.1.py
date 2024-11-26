# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

print(string.ascii_letters)
a = input()
b = int(string.ascii_letters.find(a[0]))
c = int(string.ascii_letters.find(a[-1]))
while b <= c:
    print(string.ascii_letters[b], end='')
    b += 1
