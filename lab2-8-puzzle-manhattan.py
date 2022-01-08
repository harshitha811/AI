def compare(l,l1):
 sum=0
 for i in range(3):
    for j in range(3):
        for k in range(3):
            for m in range(3):
                if(l[i][j]==l1[k][m]):
                    d=abs(i-k)+abs(j-m)
                    sum=sum+d
 return sum
def possibilities(l,l1):
 up=100
 down=100
 right=100
 left=100
 #moving up of blank space
 if(l[0][0]!=' ' and l[0][1]!=' ' and l[0][2]!=' '):
    for i in range(1,3):
        for j in range(3):
            if(l[i][j]==' '):
                m=i
                n=j
 l[m][n]=l[m-1][n]
 l[m-1][n]=' '
 up=compare(l,l1)
 l[m-1][n]=l[m][n]
 l[m][n]=' '
 #moving down of blank space
 if(l[2][0]!=' ' and l[2][1]!=' ' and l[2][2]!=' '):
    for i in range(2):
        for j in range(3):
            if(l[i][j]==' '):
                m=i
                n=j
 l[m][n]=l[m+1][n]
 l[m+1][n]=' '
 down=compare(l,l1)
 l[m+1][n]=l[m][n]
 l[m][n]=' '
 #moving right of blank space
 if(l[0][2]!=' ' and l[1][2]!=' ' and l[2][2]!=' '):
    for i in range(3):
        for j in range(2):
            if(l[i][j]==' '):
                m=i
                n=j
 l[m][n]=l[m][n+1]
 l[m][n+1]=' '
 right=compare(l,l1)
 l[m][n+1]=l[m][n]
 l[m][n]=' '
 #moving left of blank space
 if(l[0][0]!=' ' and l[1][0]!=' ' and l[2][0]!=' '):
    for i in range(3):
        for j in range(1,3):
            if(l[i][j]==' '):
                m=i
                n=j
 l[m][n]=l[m][n-1]
 l[m][n-1]=' '
 left=compare(l,l1)
 l[m][n-1]=l[m][n]
 l[m][n]=' '
 h=min(up,down,left,right)
 if(up==h):
    l[m][n]=l[m-1][n]
    l[m-1][n]=' '
    x='up'
 elif(down==h):
    l[m][n]=l[m+1][n]
    l[m+1][n]=' '
    x='down'
 elif(left==h):
    l[m][n]=l[m][n-1]
    l[m][n-1]=' '
    x='left'
 elif(right==h):
    l[m][n]=l[m][n+1]
    l[m][n+1]=' '
    x='right'
 print()
 for i in range(3):
    for j in range(3):
        print(""+l[i][j]+"|",end="")
    print()
 print("Operation performed: "+x)
 print("Manhattan distance:",h)
l=list()
#initial state
l=[['1','2','3'],[' ','4','6'],['7','5','8']]
print("\nInitial state:")
for i in range(3):
    for j in range(3):
        print(""+l[i][j]+"|",end="")
    print()
print()
print("\nNext states:")
#final state
l1=[['1','2','3'],['4','5','6'],['7','8',' ']]
while(l!=l1):
    possibilities(l,l1)
print("Goal reached")
