f = open("./bill.txt", "r", encoding="UTF_8")

# print(f.read())
for line in f:
    if "正式" in line:
        open("./bill2.txt","a",encoding="UTF_8").write(line)

f.close()
m = open("./bill2.txt","r",encoding="UTF_8")
print(m.read())
m.close()

try:
    n = open("./bl.txt", "r", encoding="UTF_8")
    print(n.read())
except Exception as e:
    print("文件不存在")
    n.open("./bl.txt", "w", encoding="UTF_8")
else:
    print("没有异常，真开心")
finally:
    print("不管有没有异常，都会执行")
    n.close()