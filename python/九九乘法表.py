#九九乘法表
for i in range(1,10):
     for j in range(1,i+1):
        if i==j:
            print("{}*{}={}".format(j,i,i*j),end="")
        else:
            print("{}*{}={}".format(j,i,i*j),end=" ")
     print()
     
