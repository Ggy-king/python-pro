a = eval(input(""))
aa = a//(24*3600)
ss = a//3600
dd = a//60
if aa == "0":
    if ss == "0":
        if dd == "0":
            print("{}秒是0天0时0分{}秒".format(a,a))
        else:
            df = a - (dd*60)
            print("{}秒是0天0时{}分{}秒".format(a,dd,df))
    else:
        sf = (a - (ss*3600))//60
        sg = a - (ss*3600) - (sf*60)
        print("{}秒是0天{}时{}分{}秒".format(a,ss,sf,sg))
else:
    ah = (a - (aa*24*3600))//3600
    ad = (a - (aa*24*3600) - (ah*3600))//60
    af = a - (aa*24*3600) - (ah*3600) - (ad*60)
    print("{}秒是{}天{}时{}分{}秒".format(a,aa,ah,ad,af))
