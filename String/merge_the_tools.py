def merge_the_tools(string, k):
    # Iterate over the string in chunks of size k
    for i in range(0, len(string), k):
        l = string[i:i+k]
        s = ""
        for alphabet in l:
            if alphabet not in s:
                s += alphabet
        print(s)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)