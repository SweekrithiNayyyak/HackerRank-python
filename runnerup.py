n=int(input())
score=input()
#split the input and store as a list
score=score.split()
new_score=[]

#to change the strings into interger
for i in range(len(score)):
    k=int(score[i])
    new_score.append(k)
#print(new_score)

#upload to same old variable
score=new_score
#decreasing order to find maximum
score.sort(reverse=True)
#print(score)

winning_score=score[0]
for _ in range(len(score)):
    if score[0]==winning_score:
        score.pop(0)

print(score[0])


