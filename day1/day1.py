# arr = ['nike', 'ale', 'bin']
# for num in arr:
#     print(num)
# print('end')
#
# a = range(1,5)
# print(a)
#
# for n in range(1,5):
#     print(n)
# print('end')

# arr = []
# l = list(range(1,10))
# print(l)
# for i in l:
#     ar = (i ** 2)
#     arr.append(ar)
# print(arr)

arr = [value ** 2 for value in range(1, 10)]
print(arr)

for i in range(1,21):
    print(i)

lf = [i ** 3 for i in range(1, 20)]
print(lf)

print(lf[:-3])

print(type(666))
print(type("好好好"))
print(type(11.11))

string = type("好好好")
int = type(666)
float = type(11.11)

# myname = input()
# print("hello " + myname)
# print(len(myname))
print(len("a b"))

while True:
    print("who are you")
    name = input()
    if(name != "nike"):
        continue
    print("hello " + name + ". what is your password?")
    password = input()
    if password == "666":
        break
print("welcome !")

