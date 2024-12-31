from collections import namedtuple
n, headers = int(input()), input().split()
Student = namedtuple('Student', headers)
print(sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n)
