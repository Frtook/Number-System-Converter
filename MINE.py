import HToB, OToB, BToH, BToO, DToB_2, BToD

b = '\033[96m'
r = '\033[91m'
y = '\033[93m'
w = '\033[m'
while True:
    Sto = input(f"{b}Enter System : D , B, O , H :{w}").lower().strip()
    n = input("Enter Numbrt : ")
    if Sto in "dboh":
        if Sto == "b":
            print(f"Oct :{y}{BToO.BO(n)}{w}")
            print(f'Hex :{y}{BToH.BH(n)}{w}')
            print(f"Dec :{y}{BToD.BD(n)}{w}")

        if Sto == "o":
            print(f"Bin :{y}{OToB.OB(n)}{w}")
            print(f"Hex :{y}{BToH.BH(OToB.OB(n))}{w}")
            print(f"Dec :{y}{BToD.BD(OToB.OB(n))}{w}")

        if Sto == "h":
            print(f"Oct :{y}{BToO.BO(HToB.HB(n))}{w}")
            print(f"Dec :{y}{BToD.BD(HToB.HB(n))}{w}")
            print(f"Bin :{y}{HToB.HB(n)}{w}")

        if Sto == "d":
            print(f"Oct :{y}{BToO.BO(DToB_2.DB(n))}{w}")
            print(f"Hex :{y}{BToH.BH(DToB_2.DB(n))}{w}")
            print(f"Bin :{y}{DToB_2.DB(n)}{w}")
    else:
        print(f"{r}Error{b}")
