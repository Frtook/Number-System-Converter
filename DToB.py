try:

    n = input()
    n = int(n)
    l = []
    a = 1
    while n > a:
        l.append(a)
        a *= 2
    if len(l) == 0:
        print('0')  # break
    l.reverse()
    b = '1'
    r = l[0]
    l.pop(0)
    for i in l:
        if r + i <= n:
            r += i
            b += '1'
        else:
            b += '0'
    print(b)
except:
    try:
        B = ''
        b = ''
        n = str(n)
        l = []
        U = []
        l = n.split('.')
        f1 = int(l[0])
        f2 = int(l[1])
        a = 1
        while f1 > a:
            U.append(a)
            a *= 2
        if len(U) == 0:
            b += '0.'
        U.reverse()
        b = '1'
        r = U[0]
        U.pop(0)
        for i in U:
            if r + i <= f1:
                r += i
                b += '1'
            else:
                b += '0'
        B += b + '.'
        U = []
        b = ''
        a = 1
        while f1 > a:
            U.append(a)
            a *= 2
        if len(U) == 0:
            b += '.'  # break
        U.reverse()
        b = '1'
        r = U[0]
        U.pop(0)
        for i in U:
            if r + i <= f2:
                r += i
                b += '1'
            else:
                b += '0'
        B += b

        print(B)
    except:
        print('Error')
        raise Exception("XX")

