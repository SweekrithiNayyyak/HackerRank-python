# Enter your code here. Read input from STDIN. Print output to STDOUT
num1=int(input())
imp1=input()
imp1=imp1.split()
num2=int(input())
imp2=input()
imp2=imp2.split()
s1=set()
s2=set()
for i in imp1:
    s1.add(int(i))

for i in imp2:
     s2.add(int(i))
l=s1.union(s2)
print(len(set(l)))