def BD(b):
    re='\033[91m'
    wh='\033[m'  
    try:
        for i in b:
            if  i not in '01.':
                print(f'{re}Value Error Enter 0 or 1 !{wh}')
                f=True
                raise Exception
        r = 0
        l = b.split('.')
        if len(l) == 1:
            l.append('.')
        c = len(l[0]) - 1
        i = 0
        while c > -1:
            r += 2 ** i * int(l[0][c])
            i += 1
            c -= 1
        if len(l[1]) > 1:
            c = 0
            i = -1
            while c < len(l[1]):
                r += 2 ** i * int(l[1][c])
                i -= 1
                c += 1
        return r
    except Exception as e :
        print(e)
        return ""
