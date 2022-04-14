ls = [0,1]
for hongban in ls:
    for hongxue in ls:
        for hongsheng in ls:
            for qiangban in ls:
                for qiangxue in ls:
                    for qiangsheng in ls:
                        for jinban in ls:
                            for jinxue in ls:
                                for jinsheng in ls:
                                    if (jinban + jinxue +jinsheng ==1)\
                                        and (hongban + hongsheng + hongxue ==1)\
                                        and (jinban + jinxue + jinsheng == 1)\
                                        and (hongban + qiangban + jinban ==1)\
                                        and (hongxue + qiangxue + jinxue == 1)\
                                        and (hongsheng + jinsheng + qiangsheng == 1):
                                        jia = (hongban + qiangsheng ==1)
                                        yi = (jinban + hongsheng ==1)
                                        bing = (qiangban + hongxue ==1)
                                        if jia + yi + bing ==3:
                                            print ('''王小红是班长:{} 李强是班长:{} 丁金是班长:{}
王小红是生活委员:{} 李强是生活委员:{} 丁金是生活委员:{}
王小红是学习委员:{} 李强是学习委员:{} 丁金是学习委员:{}'''.\
format(hongban,qiangban,jinban,\
hongsheng,qiangsheng,jinsheng,\
hongxue,qiangxue,jinxue))
