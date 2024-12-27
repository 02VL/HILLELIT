import string
def is_palindrome(text):
     text1 = text.lower()
     text2 = ""
     for i in text1:
         if i in string.punctuation or i == " ":
             continue
         else:
             text2 += i
     text3 = text2[::-1]
     if text3 == text2:
         return True
     else:
         return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
