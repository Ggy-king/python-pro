#BMI指数判断
a = eval(input("身高"))
b = eval(input("体重"))
c = b/(a*a)
if c<=18.5:
    print("体重过低")
if 18.5<c<=24:
    print("体重正常")
if 24<c<=28:
    print("体重超重")
if c>28:
    print("体重肥胖")
