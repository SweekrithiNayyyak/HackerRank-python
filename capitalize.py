#not complete
st=input()
st=list(st)
for i in range(len(st)):
    st[0]=st[0].upper()
    if(st[i]==" "):
        st[i+1]=st[i+1].upper()
    else:
        continue
new_str=""
for j in st:
    new_str+=j
print(new_str)   