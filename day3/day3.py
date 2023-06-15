message = "It was bright cold day in April"
count = {}
for i in message:
    count.setdefault(i,0)
    count[i] = count[i] + 1
print(count)

arr = "123abc1"
ary = {}
for i in arr:
    # print(i)
    ary.setdefault(i,0)
    print(ary[i])
    ary[i] += 1
print(ary)