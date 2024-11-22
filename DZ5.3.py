# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
import string
a = input()
a1 = a.title()
b = "#"
for i in a1:
    if i in string.punctuation or i == " ":
        continue
    b += i
print(b[:139])




