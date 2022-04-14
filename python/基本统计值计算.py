#基本统计值计算
def get():   #获取用户输入
    nums = []
    a = input("请输入数字，回车退出")
    while a != "":
        nums.append(eval(a))
        a = input("请输入数字，回车退出")
    return nums

def mean(numbers):   #计算平均值
    s = 0.0
    for i in numbers:
        s = s + i
    return s / len(numbers)

def dev(numbers,mean):  #计算方差
    s = 0.0
    for i in numbers:
        s = s + (i - mean) ** 2
    return pow(s / (len(numbers)-1),0.5)

def median(numbers):   #计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2]) / 2
    else:
        med = numbers[size//2]
    return med
n = get()
m = mean(n)
print("平均值；{},方差：{:.2},中位数：{}.".format(m,dev(n,m),median(n)))
    
    
