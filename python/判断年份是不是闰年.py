#闰年： 四年一闰，百年不闰，四百年再闰
year = int(input("请输入一个年份： "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0}是闰年".format(year))
        else :
            print("{0}不是闰年".format(year))
    else :
        print("{0}是闰年".format(year))
else :
    print("{0}不是闰年".format(year))
