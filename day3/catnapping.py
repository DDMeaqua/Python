import os
import re
import shelve

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
print(password.isdecimal())  # 纯数字

title = "Good"
print(title.istitle())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('my number is 415-555-4242')
print('phone number found:' + mo.group())

print(os.getcwd())

# os.path.getsize('/documents/Connect-AI/feishu-openai')
baconFile = open("bacon.txt", "w")
baconFile.write('Hello world! \n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not vegetable.')
baconFile.close()
baconFile = open("bacon.txt")
content = baconFile.read()
baconFile.close()
print(content)

shelfFile = shelve.open('mydata')
cats = ['zophie', 'pooka', 'simon']
shelfFile['cats'] = cats
shelfFile.close()


def message(name, age, love):
    print("姓名：" + name + "，年龄：" + age + "，爱好：" + love)

message('小明', '18', "game")
message(name="aaa",love="haha",age="100")

