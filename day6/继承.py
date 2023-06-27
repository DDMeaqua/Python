class Phone:
    IMEI = None
    producer = "Apple"

    def call_by_4g(self):
        print("4G通话")

class Phone2023(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2023新功能：5G通话")

# phone = Phone2023()
#
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()

# 演示多继承
class NFC:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("读卡")
    def write_card(self):
        print("写卡")

class RemoteControl:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控 开启")

class MyPhone(Phone2023, NFC, RemoteControl):
    pass

my_phone = MyPhone()
my_phone.call_by_5g()
my_phone.read_card()
my_phone.write_card()
my_phone.control()
print(my_phone.nfc_type)
print(my_phone.producer)    # 多继承，同名按照左边优先继承


