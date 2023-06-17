def test(compute):
    result = compute(1, 2)
    print(f"计算结果为：{result}")


test(lambda x, y: x + y)

test(lambda i, j: i * j)
