# 函数open（），参数为需要打开的文件的名称
# 关键词with，在不再需要访问文件后将其关闭
# 方法read(),读取文件全部内容
file_path = r'C:\Users\HP\Documents\Python_Work\text_files\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(r'text_files\pi_digits.txt') as file_object:
    contents = file_object.read()
    for line in file_object:
        print(line)

with open(r'text_files\pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

with open(r'text_files\pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52])
print(len(pi_string))

# 圆周率中包含你的生日吗？
birthday = input('\nPlease enter your birthday in mmddyy: ')
if birthday in pi_string:
    msg = 'Your birthday appears in the first million digits of pi.'
    print(msg)
else:
    msg = 'Your birthday does not appear in the first million digits of pi.'
    print(msg)


