s=input()
if len(s)!=5:
    s=print("输入有误！")
else:
    if eval(s[::-1])==eval(s):
        print("True")
    else:
        print("False")
