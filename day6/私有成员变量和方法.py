class Phone:
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让cpu单核模式运行")

    def _call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5G通话")
        else:
            self.__keep_single_core()
            print("电压不足，无法5G通话,并设置为单核运行省电模式")


phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)

phone._call_by_5g()