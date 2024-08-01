import sys
n, m = map(int, sys.argv[1:3])
i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break