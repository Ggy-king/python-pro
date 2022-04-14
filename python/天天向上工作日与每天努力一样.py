#天天向上工作日得努力到什么地步才能与每天努力一样
def UP(df):
    up = 1.0
    for i in range(365):
        if i % 7 in [6,0]:
            up = up * (1 - 0.01)
        else:
            up = up * (1 + df)
    return up
df = 0.01
while (UP(df)<37.78):
    df += 0.001
print("每天的努力参数是：{:.3f}".format(df))
