# 函数open（），参数为需要打开的文件的名称
# 关键词with，在不再需要访问文件后将其关闭
# 方法read(),读取文件全部内容
file_path = r'C:\Users\HP\Documents\Python_Work\text_files\pi_million_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# Is your birthday contained in the first million digits of Pi？
birthday = input('\nPlease enter your birthday in mmddyy: ')
if birthday in pi_string:
    msg = 'Your birthday appears in the first million digits of pi.'
    print(msg)
else:
    msg = 'Your birthday does not appear in the first million digits of pi.'
    print(msg)
