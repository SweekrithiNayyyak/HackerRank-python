# Enter your code here. Read input from STDIN. Print output to STDOUT
n=set(map(int,input().split()))
l=[]
for i in range(int(input())):
    l.append(set(map(int,input().split())))
    
for members in l:
    if members.issubset(n) and len(members)!=len(n):
        continue
    else:
        print("False")
        break
else:
    print("True")
