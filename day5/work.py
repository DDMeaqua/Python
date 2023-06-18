import my_utils.str_util
import my_utils.file_util

print(my_utils.str_util.str_reverse("hello"))

print(my_utils.str_util.substr("hello", 1, 6))

my_utils.file_util.print_file_info("bill2.txt")
my_utils.file_util.addend_to_file("bill2.txt", "\n hello world \n")

print("-------------------")
print(open("bill2.txt", "r").read())