import os
import re

print('''Dear Alice,
Eva's cat has been arrested for catnapping
Sincerely,
Bob
''')

"""
多
行
注
释
"""
print("""多
行
注
释""")

arr = "How are you?"
arr.upper()
print(arr)
arr = arr.upper()
print(arr)

password = '123456'
print(password.isdecimal())     #纯数字

title = "Good"
print(title.istitle())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('my number is 415-555-4242')
print('phone number found:' + mo.group())

print(os.getcwd())
