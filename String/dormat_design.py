
a,b=map(int,input().split())
pattern = 1
rows = b // 2 - 1
middle_rows=b//2-3
for lines in range(a):
    if lines == a // 2:
        print("-" * (middle_rows) + "WELCOME" + "-" * (middle_rows))
        rows += 3
        pattern -= 2
        continue

    print("-" * rows + ".|." * pattern + "-" * rows)
    
    if lines < a // 2:
        rows -= 3
        pattern += 2
    else:
        rows += 3
        pattern -= 2