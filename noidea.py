happiness=0
length=input().split()

l=[]
for i in length:
    p=int(i)
    l.append(p)
length=l

elementsOfArray=input().split()

e=[]
for i in elementsOfArray:
    p=int(i)
    e.append(p)
elementsOfArray=e

set1=input().split()

s1=[]
for i in set1:
    p=int(i)
    s1.append(p)
set1=s1

set2=input().split()

s2=[]
for i in set2:
    p=int(i)
    s2.append(p)
set2=s2
    

for i in elementsOfArray:
    for j in set1:
        if i==j:
            happiness+=1
    for k in set2:
        if i==k:
            happiness-=1
    
print(happiness)
    


