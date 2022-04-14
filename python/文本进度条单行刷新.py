#文本进度条单行动态刷新
import time
for i in range(101):
    print("\r{:3}%".format(i),end = "")#\r 是转义符把光标定回元首
    time.sleep(0.01)
