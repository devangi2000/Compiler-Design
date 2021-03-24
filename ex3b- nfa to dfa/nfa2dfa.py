NFA=[]
DFA1=[]
DFA=[]
while 1:
    st = input("Enter the Regular Expression and Q to exit: ")
    if(st=='0'):
        break
    if(len(st)==1):
        print("NFA : "+"0 "+st+" 1")
        print("DFA : "+"0 "+st+" 1")
    if(len(st)==2):
        if(st[1]=='*'):
            NFA = ("0 e 1 "+st[0]+" 2 e 3 0 e 3 2 e 1")
            print("NFA : "+NFA)
            # print(NFA[0])
            for i in range (0, len(NFA)):
                # print(i)
                if(NFA[i]==st[0]):
                    DFA1 = (NFA[i-2]+" "+NFA[i]+" "+NFA[i+2])
                    print("DFA : "+DFA1)
                    break
        else:
            print("NFA : "+"0 "+st[0]+" 1 "+st[1])
            print("DFA : "+"0 "+st[0]+" 1 "+st[1])
    if(len(st)==3):
        NFA=("0 e 1 "+st[0]+" 2 e 5 0 e 3 "+st[2]+" 4 e 5")
        print("NFA : "+NFA)
        for i in range(0, len(NFA)):
            if (NFA[i]==st[0]) or (NFA[i]==st[2]):
                DFA1 = (NFA[i-2]+" "+NFA[i]+" "+NFA[i+2])
                DFA.append(DFA1)
        print('DFA : '+' '.join(DFA))
        DFA=[]
    if st=='Q':
        break