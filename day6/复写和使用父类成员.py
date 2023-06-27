class Phone:
    IMEI = None
    producer = "Apple"

    def call_by_5g(self):
        print("5G通话")

class MyPhone(Phone):
    producer = "HTC"

    def call_by_5g(self):
        print("开启CPU单核模式")
        print("4G通话")
        # 方式1
        Phone.call_by_5g(self)      # 调用父类的方法
        # 方式2
        print(f"父类多厂商是：{super().producer}")


my_phone = MyPhone()
print(my_phone.producer)
my_phone.call_by_5g()
