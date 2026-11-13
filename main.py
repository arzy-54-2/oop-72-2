# import module1

# from module1 import *
#
# print(add(12, 12))
# print(test_var)
# # print(random.randint(1, 10))


# from my_package.module1 import *
# from my_package.module2 import var_module_2
# from my_package import var_module_2, test_var
#
# print(test_var)
# print(var_module_2)
# from lesson.lesson1 import Hero
#
#
# ardager = Hero("NAme", 100, 100)
#
# ardager.action()
from my_package import add
print(add(24, 12))


print("TEXT")
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')