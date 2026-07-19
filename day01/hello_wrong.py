from datetime import date
import platform
name=input("请输入你的姓名：")

print("你好,"+name+"!")
print("当前python版本:",platform.python_version())
print("今天日期:",date.today())