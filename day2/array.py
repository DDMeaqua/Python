eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)

def fun():
    print(eggs)

fun()

# 列表（数组）
arr = [1,"a","b"]

# 元组
tup = (1,"a","b")

# str
ary = "hello"

# 数组转元组
print(tuple(arr))

# 元组转数组
print(list(tup))

# str转数组
print(list(ary))

spam = [0,1,2,3,4]
cheese = spam
cheese[1] = 10
print(spam)
print(cheese)

birthdays = {"alice":"Apr 1","bob":"Dec 12","carol":"Mar 4"}

while True:
    print("Enter a name (blank to quit)")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("我没有这个生日信息关于这个名叫：" + name)
        print("what is their birthday ?")
        bday = input()
        birthdays[name] = bday
        print(name + " 的 " + bday + " 生日已经记录")