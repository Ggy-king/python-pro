"""用python设计的第一个游戏"""
counts = 3
while counts > 0:
  temp=input("你敢猜猜老子现在心里想的数字是什么")
  guess=int(temp)

  if guess==6:
    print("你竟然猜对了")
    print("猜对了也没有用，该还钱还是得还钱")
    break
  else:
      if guess < 6:
        print("小了傻子")
      else:
        print("大了傻逼")
      counts = counts - 1

print("游戏结束，不用玩了")
    
