def agent():
 dic = dict()
 print("Enter the status of the locations: 0 for clean and 1 for dirty")
 s1 = int(input("A\n"))
 s2 = int(input("B\n"))
 dic['A'] = s1
 dic['B'] = s2
 l = input("Enter the first location\n")
 while (1):
    if (l == 'A'):
        if (dic['A'] == 1):
            print("Action: Suck the dirt")
            dic['A'] = 0
        else:
            print("No action in A")
        if (dic['B'] == 1):
            print("Action: Move right to B")
            l = 'B'
        else:
            print("Goal reached. Both the locations are clean")
            break
    else:
        if (dic['B'] == 1):
            print("Action: Suck the dirt")
            dic['B'] = 0
        else:
            print("No action in B")
        if (dic['A'] == 1):
            print("Action: Move left to A")
            l = 'A'
        else:
            print("Goal reached. Both the locations are clean")
            break
print('_____ _____')
print('| | | |')
print('| Location A | | Location B |')
print('| | | |')
print('|____| |_____|')
print()
agent()
##########
def agent():
 dic = dict()
 nol = int(input("Enter the number of loactions\n"))
 print("Enter the status of the locations: 0 for clean and 1 for dirty")
 for i in range(nol):
    s = int(input())
    dic[i + 1] = s
    l  = 1
 while (1):
    if (dic[l] == 1):
        print("Action: Suck the dirt")
        dic[l] = 0
    else:
        print("Action: No operation")
    if (l != nol):
        print("Action: Move to the next location")
        l = l + 1
    if (l > nol):
        break
 print("Goal reached. All the lsocations are clean")
agent()
