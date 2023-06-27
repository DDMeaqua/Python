class Student:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

    def __str__(self):
        return f"Student类对象，name：{self.name} ，age：{self.age} ，tel：{self.tel}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("张三", 18, "123456789")
print(stu1.name)
print(stu1.age)
print(stu1.tel)

print(stu1)
# print(str(stu1))

stu2 = Student("李四", 18, "987654321")
print(stu1 <= stu2)
print(stu1 >= stu2)