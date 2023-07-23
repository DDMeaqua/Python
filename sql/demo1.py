from pymysql import Connection
# 获取mysql链接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='',
    autocommit=True,
)
# 打印mysql信息
# print(conn.get_server_info())

curses = conn.cursor()
conn.select_db("xz")

curses.execute("insert into xz_user values(5, 'ak47', '123456', 'ming@qq.com', '13501234560', 'img/avatar/default.png', 'gun', 1)")
# #手动确认
# conn.commit()

curses.execute("select * from xz_user")
res = curses.fetchall()
for r in res:
    print(r)
# 关闭链接
conn.close()
