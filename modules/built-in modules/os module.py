import os

# # To get path of current working directory
# print(os.getcwd())


# # To create directory
# os.mkdir('C:\Users\gopik\PycharmProjects\Python-Class\modules\newdir')   # --> this makes a unicode error (takes \n as new line)
#                                                                     # so need to use raw string(r) to treat special characters from the path
# os.mkdir(r'C:\Users\gopik\PycharmProjects\Python-Class\modules\newdir')
# print('New Directory Created')

#     # using user input
#
# dir=input('Enter the new directory name:')
# os.mkdir(r'C:\Users\gopik\PycharmProjects\Python-Class\modules\{dir}')   # --> this will create a directory with name '{dir}
#                                                                      # so need to use formatting string(f) to add variables to the path/string
# os.mkdir(rf'C:\Users\gopik\PycharmProjects\Python-Class\modules\built-in modules\{dir}')
# print('New Directory Created')


# # To list files inside a directory
# print(os.listdir(r'C:\Users\gopik\PycharmProjects\Python-Class\patterns'))


# # To remove an empty directory
# os.rmdir(r'C:\Users\gopik\PycharmProjects\Python-Class\modules\{dir}')
# os.rmdir(r'C:\Users\gopik\PycharmProjects\Python-Class\modules\built-in modules\mydir')
# os.rmdir(r'C:\Users\gopik\PycharmProjects\Python-Class\modules\newdir')
# print('Directory Removed')


# # To delete a file
# os.remove(r'path.......')