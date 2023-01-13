if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        m=input()
        m.strip()
        k=m.split()
        if(k[0]=="insert"):
            k1=int(k[1])
            k2=int(k[2])
            l.insert(k1,k2)
        elif(k[0]=="append"):
            k1=int(k[1])
            l.append(k1)
        elif(k[0]=="print"):
            print(l)
        elif(k[0]=="remove"):
            k1=int(k[1])
            l.remove(k1)
        elif(k[0]=="pop"):
            l.pop()
        elif(k[0]=="sort"):
            l.sort()
        elif(k[0]=="reverse"):
            l[::-1]
        else:
            print("error")