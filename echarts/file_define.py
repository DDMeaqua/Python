"""
和文件相关的定义
"""
import json
from data_define import Record

class FileReader:
    def read_data(self) -> list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path    # 文件路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileRecord(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="utf-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            Record(data_dict["data"], data_dict["order_id"], data_dict["money"], data_dict["city"])

        f.close()
        return record_list


if __name__ == '__main__':
    text_reader = TextFileReader("data.txt")
    json_reader = JsonFileRecord("datajson.txt")

    list1 = text_reader.read_data()
    list2 = json_reader.read_data()

    print(list2)