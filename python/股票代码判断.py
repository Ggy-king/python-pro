
###代码开始
#股票代码判断
a = input("股票代码")
while a not in ["000000"]:
    if a[0:2] in ['60']:
      print("沪市A股")
    if a[0:3] in ['000']:
      print("深市A股")
    if a[0:3] in ['002']:
      print("中小板")
    if a[0:3] in ['300']:
      print("创业板")
    if a[0:3] in ['688']:
      print("科创板")
    if a[0:3] in ['123','788']:
        print("错误编码")
    a = input("股票代码")
  
