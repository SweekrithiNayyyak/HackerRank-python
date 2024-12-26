# Enter your code here. Read input from STDIN. Print output to STDOUT
count=1
k=input()
for i in range(1,len(k)):
    if k[i]!=k[i-1]:
        print(f"{count, int(k[i-1])}",end=" ")
        count=1
    else:
        count+=1
print(f"{count,int(k[-1])}")
print()
