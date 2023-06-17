f = open("../day3/bacon.txt","r",encoding="UTF_8")

n = open("../day3/bacon.txt","a")

print(type(f))
print(type(n))

# print(f"read的方法读取全部内容结果是：{f.read()}")
print("------------------------")

# 读取文件全部行，封装到列表
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 注释防止指针,下面证明指针的存在
lines1 = f.readline()
lines2 = f.readline()
lines3 = f.readline()
print(lines1)
print(lines2)
print(lines3)
print("-------------------------")

e = open("./demo.txt","r",encoding="UTF_8")
# 方式一 读取全部内容，通过字符串count方法统计itheima单词数
# count = e.read().count("itheima")
# print(f"itheima单词出现的次数是：{count}次")


# 方式二 读取内容，一行一行读
num = 0
for line in e:
    line = line.strip()  # 去除空格 \n换行符
    worrds = line.split(" ")  # 以空格为分隔符，将字符串分割成列表
    print(worrds)
    for word in worrds:
        if word == "itheima":
            num += 1
print(f"itheima单词出现的次数是：{num}次")
e.close()

