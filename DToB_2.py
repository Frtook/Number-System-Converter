def DB(a):
    try:
        b=''
        sp=a.split(".")
        if len(sp) ==1:
            l=[]
            w=int(sp[0])
            while w>2:
                if w>2:
                    l. append(w%2)
                    w=int(w/2)
            if w<2:
                l.append(w)
            for i in (l[::-1]):
                b+=str(i)
        elif len (sp)>1 :
            lst1=[]
            l=[]
            w=int (sp[0])
           # print (w)
            while w>2:
                # if w>8 :
                    #print (w)
                l.append (w%2)
                w=int (w/2)
            if w<2:
                l.append(str(w))
            for i in (l[::-1]):
                lst1. append (i)
            lst1. append (".")
            ln=len(sp[1])
            y=((int (sp[1 ]))/(10**ln))
            l2=[]
            for u in range(0, 100):
                if y % 1 != 0:

                    g=y*2
                    s=str(g)
                    z=s.split(".")
                    siz=len(z[1])
                    h=int(z[1])
                    y=(h/(10**siz))
                    lst1.append(int(z[0]))
            for o in (lst1):
                b+=str(o)
        return b
        print()
    except:
        print("Error")