import string
from pickletools import string1
from string import ascii_letters


def first_word(text):
    """ Пошук першого слова """
    # perevirka = string.punctuation.replace("'")
    # text1 = text.replace(string.punctuation, ' ')
    # text1 = text.split()
    # text2 = text1[0]
    str1 = ""
    c = 0
    ind1 = 0
    for i in text:
        if i.isalpha():
            ind1 = text.find(i)
            break

    for i in text[ind1:]:
        if i == " " or i == "," or i == ".":
            return str1
        str1+=i
    return str1

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
