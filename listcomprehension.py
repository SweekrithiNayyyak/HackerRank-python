x = int(input())
y = int(input())
z = int(input())
n = int(input())
l=[]
    
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            #make all possible combinations
            l.append([i,j,k])

#print(l)

sum=0
#to store sum of all the numbers
new_l=[]
#iterate through the lenth of the combinations
for b in range(len(l)):
    for inda in [0,1,2]:
        #each index with have three subindexes
        #add them
        sum+=l[b][inda]
    #print(b,sum)
    #store the sum in a list
    new_l.append(sum)
    #resetsum to 0 
    sum=0
        
#print(new_l)
#to store the new lis whose sum is not equal to given n
an_new=[]
#iterate through the list containing sum 
for elex in range(len(new_l)):
    #check if element(sum) is equal tot he mentioned number
    if new_l[elex]!=n:
        #when they are not equal append the elements correspoding to the index into the new list
        an_new.append(l[elex])
#display the new list
print(an_new)
