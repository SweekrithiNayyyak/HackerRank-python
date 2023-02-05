# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=input().split()
s=set()

for i in m:
    s.add(int(i))

l=int(input())
for j in range(l):
    ns=set()
    com=input().split()
    nsk=input().split()
   
    for k in nsk:
        ns.add(int(k))
    if com[0]=="intersection_update":
        s.intersection_update(ns)
    if com[0]=="update":
        s.update(ns)
    if com[0]=="symmetric_difference_update":
        s.symmetric_difference_update(ns)
    if com[0]=="difference_update":
        s.difference_update(ns)
print(sum(s))
        
    
    
        
    
        
    
    
    

    