#该天天向上中用变量表示每天努力多少
import math
a = 0.01
up = math.pow((1.0 + a),365)
down = math.pow((1.0 - a),365)
print("向上：{:.2f},向下：{:.2f}".format(up,down))
