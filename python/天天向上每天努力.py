#天天向上每天努力
import math
dayup = math.pow((1.0 + 0.001),365) #提高0.001
daydown = math.pow((1.0 - 0.001),365) #放任0.001
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))
