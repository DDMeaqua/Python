# my_list: list = [1, 2, 3, 4, 5]
# my_tuple: tuple = (1, 2, 3, 4, 5)
# my_dict: dict = {"name": "张三", "age": 18}
# my_set: set = {1, 2, 3, 4, 5}
# my_str: str = "hello world"
import json

# 详细注解
my_list: list[int] = [1, 2, 3, 4, 5]
my_tuple: tuple[int, str, bool] = (1, "hello", True)
my_dict: dict[str, str] = {"name": "张三", "age": "18"}
my_set: set = {1, 2, 3, 4, 5}
my_str: str = "hello world"

var_1 = random.randint(1, 10)  # type
var_2 = json.load('{"name": "张三"}')
def func():
    return 10
var_3 = func()   # type int