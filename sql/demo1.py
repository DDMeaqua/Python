from pymysql import Connection
# 获取mysql链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='',
)
# 打印mysql信息
print(conn.get_server_info())
# 关闭链接
conn.close()
