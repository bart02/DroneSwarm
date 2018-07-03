x = int(input())
y = int(input())
first = int(input()) - 1
Mx = []
My = []
for e in range(x):
    for i in range(y):
        My.append(first + 1)
        first+=1
    Mx.append(My)
    My = []

print("[", end='')
for i in range(y):
    for e in range(x):
        if (i == y-1 and e == x-1):
            print(Mx[e][i], end='')
        else:
            print(Mx[e][i], end=', ')
    if (i != y-1):
        print()
print("]")
