import os
libs = {'numpy','matplotlib','pillow','sklearn','requests',\
        'jieba','beautifulsoup4','wheel','networkx','sympy','pyinstaller',\
        'django','flask','werobot','PyQt5','pandas','pyopengl',\
        'pypdf2','docopt','pycame'}
try :
    for lib in libs:
        os.system('pip install '+lib)
    print('成功')
except:
    print('失败')
