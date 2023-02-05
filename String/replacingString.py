def mutate_string(string, position, character):
    l=list(string)
    l[position]= c
    #removing the commas from the list to turn it to a string
    string= ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
