
from time import sleep


def func1():
    print("func1 start")
    num = 1/0
    print("func1 end")

def func2():
    print("func2 start")
    func1()
    print("func2 end")

def main():
    try:
        func2()
    except Exception as e:
        print(e)

main()

print("你好")
sleep(1)
print("你好")
# print(time.gmtime())

import mymodel
mymodel.test(1,2)
mymodel.ts(4,5)