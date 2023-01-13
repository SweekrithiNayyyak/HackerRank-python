l=[]
for _ in range (int(input())):
    name=input()
    score=float(input())
    l.append([score,name])

l.sort()
#print(len(l))
first_minimum=l[0][0]
for _ in range(len(l)):
    if l[0][0]==first_minimum:
        l.pop(0)
#print(l)
#print(len(l))

second_minimum=l[0][0]
new_l=[]
for _ in range(len(l)):
    if(l[0][0]==second_minimum):
        new_l.append(l.pop(0))
#print(new_l)
for i in range(len(new_l)):
    print(new_l[i][1])
