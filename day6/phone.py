class Phone:
    # 提供私有成员变量
    __is_5g_enable = True  # 5G状态

    # 提供私有成员方法
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G")

    # 提供公开成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()

