# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

import random
lst = []
a = random.randint(3, 10)
for i in range(a):
    lst.append(random.randint(1,10))

lst1 = [lst[0], lst[2], lst[-2]]
print(lst)
print(lst1)