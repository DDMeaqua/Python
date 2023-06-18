# import my_package.my1
# import my_package.my2
#
# my_package.my1.info_print1()
# my_package.my2.info_print2()

# from my_package import my1
# from my_package import my2
# my1.info_print1()
# my2.info_print2()

from my_package.my1 import info_print1
from my_package.my2 import info_print2
info_print1()
info_print2()