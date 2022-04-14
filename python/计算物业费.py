a = input("类型")
b = input("面积")
c = input("月数")
if a in ["1"]:
    if eval(c)<12:
        f = eval(b)*eval(c)*0.8
    else:
        f = eval(b)*eval(c)*0.8*0.95
    print("物业费{:.2f}".format(f))
if a in ["2"]:
    if eval(c)<12:
        f = eval(b)*eval(c)*1.8
    else:
        f = eval(b)*eval(c)*1.8*0.95
    print("物业费{:.2f}".format(f))
if a in ["3"]:
    if eval(c)<12:
        f = eval(b)*eval(c)*3
    else:
        f = eval(b)*eval(c)*3*0.95
    print("物业费{:.2f}".format(f))
