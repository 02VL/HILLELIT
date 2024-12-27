def prime_generator(end):
    b = 2
    while b < end+1:
        z = 2
        k = 0
        while z<b:
            if b%z == 0:
                k = 1
                break
            else:
                z+=1
        if k == 0:
            yield b
            b+=1
        else:
            b+=1

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
