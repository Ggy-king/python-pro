#货币转换
aa = input("请输入数值")
if aa[0] in ['I'] :
  c = eval(aa[2:])*2.54
  print("CM{:.2f}".format(c))
elif aa[1] in ['M'] :
  d = eval(aa[2:])*0.393700787402
  print("IN{:.2f}".format(d))
else :
  print("输入不符合要求！")
