#rod chr
a = input("")
for i in a:
    if ord("o")<ord(i)<ord("q"):
        print(chr(ord(i)-32),end = '')
    elif ord("n")<ord(i)<ord("p"):
        print(chr(ord(i)-32),end = '')
    else:
        print(i,end = '')
        
