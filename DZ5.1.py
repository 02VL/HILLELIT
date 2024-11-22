# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True


import keyword
result = True
a = input('назва змінної має задовільняти наступні вимоги: \n Змінна не може:\n - починатися з цифри\n - містити великі літери, \n - пробіл і знаки пунктуації, окрім нижнього підкреслення "_". \n - бути жодним із зареєстрованих слів \n\n введіть назву змінної: ')
b = a[0]
if a in keyword.kwlist:
    result = False
elif b.isdigit():
    result = False
if a.find("_", 1) == 1 and a[0] == "_":
    result = False
for i in a:
    if i.isupper():
        result = False
    if i.isalnum() or i == "_":
        continue
    else:
        result = False

print(result)