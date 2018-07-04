from __future__ import print_function

x = int(input("X: "))
y = int(input("Y: "))
l = int(input("Length of column: "))
first = int(input("First: ")) - 1
Mx = []
My = []
O = []
for ll in range(x/l):
    for e in range(y):
        for i in range(l):
            Mx.append(first + 1)
            first += 1
        My.append(Mx)
        Mx = []
    O.append(My)
    My = []

print("[")
for e in range(len(O[0])):
    for j in range(len(O)):
        for q in O[j][e]:
            if e == len(O[0]) - 1 and j == len(O) - 1 and q == O[j][e][len(O[j][e])-1]:
                print(q, end='')
            else:
                print(q, end=', ')
    print()
print("]")
