#!/usr/bin/python3
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
针对第一行的解释
	（1）如果调用python脚本时，使用:python script.py，"#!/usr/bin/python" 被忽略，等同于注释。
	（2）如果调用python脚本时，使用:./script.py，"#!/usr/bin/python" 指定解释器的路径。通常在 Linux 上有作用
'''
print('演示输入输出-----------------------')
name = input('please enter your name: ')
print('Hello,', name)
# ord获取字符的整数-65
print(ord('A'))
# chr转换为对应的字符-'B'
print(chr(66))

print('演示循环---------------------------')
# 行与缩进演示，and/or/not
if True and False:
    print("False")
else:
    print("True")

print('------------------------------')
"""
 字符串演示
"""
print("字符串演示:");
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str='Runoob'

print(str)                 # 输出字符串
print( str, end=" " )        # 输出不换行
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print('hello\nrunoob')     # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')    # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print('------------------------------')
print("等待用户输入演示");
input("\n\n按下 enter 键后退出。")       # "\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。


print('------------------------------')
print("import 与 from...import演示");
# 导入 sys 模块
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
# 导入 sys 模块的 argv,path 成员
from sys import argv,path  #  导入特定的成员

print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

