###### 统计投票结果，请在下面标注序号的位置添加程序 #####
#输入一行姓名，用空格分隔
nameStr = input()

#(1)将字符串转换为列表nameList，每个姓名为一个元素

nameList = nameStr.split( )

print(nameList)
#(2)创建一个空字典 count
a = {}

#(3)统计列表中每个姓名出现的次数，用字典表示（name:num）
for i in nameList:
    a[i] = nameList.count(i)

#输出统计结果，每行输出一个： 姓名：票数
for item in a:
    print('%s:%d'%(item,a[item]))
    
###### 程序结束#####
