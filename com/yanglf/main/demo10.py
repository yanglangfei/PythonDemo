import os
import uuid

cur_path = os.getcwd()
print('当前目录:{}'.format(cur_path))
os_path = os.path
print('py lib 目录:{}'.format(os_path))
# 子目录
print(os.listdir(cur_path))
# 是否是文件
print(os.path.isfile(cur_path))

# 读写模式：
# r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件
# 常用读写模式
# 如:'rb','wb','r+b'等等
# 读写模式的类型有：
# rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
# w      以写方式打开，
# a      以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# r+     以读写模式打开
# w+     以读写模式打开
# a+     以读写模式打开
# rb     以二进制读模式打开
# wb     以二进制写模式打开
# ab     以二进制追加模式打开
# rb+    以二进制读写模式打开
# wb+    以二进制读写模式打开
# ab+    以二进制读写模式打开
# W      若文件存在，首先要清空，然后重新创建文件
# a      把所有的数据追加到文件的尾部，即使seek指在其他的位置，如果文件不存在，则重新创建

if not os.path.exists('../f'):
    os.makedirs('../f')
f = open('../f/test.txt', mode='wb+')
f.write(('hello   ' + str(uuid.uuid4()) + "  \n").encode('utf-8'))
f.flush()
# 写完之后  光标在末尾  需要移到第一行
f.seek(0, 0)
print(f.read())
# 当前光标所在位置
print(f.tell())
# 方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
# 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
position = f.seek(10, 0)
print(f.tell())
print(position)
# 在指定位置写入 字符串
f.write('POPOPOPO'.encode('utf-8'))
f.flush()

# 切换目录
os.chdir('c:/')
print(os.getcwd())
# 帮助文档
# print(help(os))
# 数据类型
print(type(os))
