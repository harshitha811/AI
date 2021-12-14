def printing(l):
    for i in range(3):
        for j in range(3):
            print(""+l[i][j]+"|",end="")
        print()

def func(l,cell):   
    l[(cell-1)//3][(cell-1)%3]='1'
    print()
    printing(l)
    print()

    for k in range(3):
        p=0
        for i in range(3):
            if(l[k][i]=='0'):
                p=p+1
            else:
                j=i
        if(p==2 and l[k][j]==' '):
            l[k][j]='0'
            printing(l)
            print("0 has won")
            quit()
            return


    for k in range(3):
        p=0
        for i in range(3):
            if(l[i][k]=='0'):
                p=p+1
            else:
                j=i
        if(p==2 and l[j][k]==' '):
            l[j][k]='0'
            printing(l)
            print("0 has won")
            quit()
            return

    p=0
    for i in range(3):
        if(l[i][i]=='0'):
            p=p+1
        else:
            j=i
    if(p==2 and l[j][j]==' '):
        l[j][j]='0'
        printing(l)
        print("0 has won")
        quit()
        return

    #check diag2
    p=0
    if(l[0][2]=='0'):
        p=p+1
    else:
        m=0
        n=2
    if(l[1][1]=='0'):
        p=p+1
    else:
        m=1
        n=1
    if(l[2][0]=='0'):
        p=p+1
    else:
        m=2
        n=0

    if(p==2 and l[m][n]==' '):
        l[m][n]='0'
        printing(l)
        print("0 has won")
        quit()
        return


    p=0
    for i in range(3):
        if(l[(cell-1)//3][i]=='1'):
            p=p+1
        else:
            j=i
    if(p==2 and l[(cell-1)//3][j]==' '):
        l[(cell-1)//3][j]='0'
        printing(l)
        return

    p=0
    for i in range(3):
        if(l[i][(cell-1)%3]=='1'):
            p=p+1
        else:
            j=i
    if(p==2 and l[j][(cell-1)%3]==' '):
        l[j][(cell-1)%3]='0'
        printing(l)
        return


    if(((cell-1)//3==(cell-1)%3) or ((cell-1)//3+(cell-1)%3==2)):#check diag also

        if((cell-1)//3==(cell-1)%3):
            p=0
            for i in range(3):
                if(l[i][i]=='1'):
                    p=p+1
                else:
                    j=i
            if(p==2 and l[i][j]==' '):
                l[j][j]='0'
                printing(l)
                return

        elif((cell-1)//3+(cell-1)%3==2):
            p=0
            if(l[0][2]=='1'):
                p=p+1
            else:
                m=0
                n=2
            if(l[1][1]=='1'):
                p=p+1
            else:
                m=1
                n=1
            if(l[2][0]=='1'):
                p=p+1
            else:
                m=2
                n=0

            if(p==2 and l[m][n]==' '):
                l[m][n]='0'
                printing(l)
                return


    if(l[1][1]==' '):
        l[1][1]='0'
        printing(l)
        return

    else:
        for i in range(3):
            for j in range(3):
                if(l[i][j]==' '):
                    l[i][j]='0'
                    printing(l)
                    return


l=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

c=0
while(c<5):
    c=c+1
    print("\nCell numbers:")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
    print()
    cell=int(input("Enter the cell number\n"))
    if(l[(cell-1)//3][(cell-1)%3]==' '):
        func(l,cell)
    else:
        print("This cell is already occupied")
        c=c-1

print("Game drawn")
