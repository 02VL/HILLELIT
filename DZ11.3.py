def is_even(number):
    list1 = [0,2,4,6,8]
    number1 = str(number)
    number1 = number1[-1]
    number1 = int(number1)
    if number1 in list1:
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("Thank you")