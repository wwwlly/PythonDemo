# -*- coding: UTF-8 -*-
import os

print "demo"
print os.getcwd()

file_path = __file__
dirname = os.path.dirname(__file__)
print __file__
print dirname
print os.path.abspath(file_path)
print os.path.abspath("G:\GitRepository\PythonDemo\png")

for letter in 'Python':
   print 'letter :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
   print 'fruit :', fruit
   
def testFor():
  for letter in 'Python':
   print 'letter :', letter
  return

#testFor()

devices = os.system("adb devices")
print devices

# 定义函数
def printme( str ):
   "打印任何传入的字符串"
   print str
   return
 
# 调用函数
printme("www")
#中文报错
#printme("测试")