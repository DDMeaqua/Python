def print_file_info(file_name):
    try:
        f = open(file_name, "r")
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        f.close()

f = None
def addend_to_file(file_name,data):
    try:
        f = open(file_name, "a")
        f.write(data)
        f.write("\n")
        f.close()
    except Exception as e:
        print(e)
        f = open(file_name, "w").write(data)
    finally:
        f.close()


# print_file_info("../day5/bill.txt")
# addend_to_file("./aaa.txt", "hello world")