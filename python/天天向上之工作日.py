#天天向上之工作日，五天工作，两天晒网
up,a = 1.0,0.01
for i in range(365):
    if i % 7 in [6,0]:
        up = up * (1 - a)
    else:
        up = up * (1 + a)
print("向上5天向下两天的力量是{:.2f}".format(up))
