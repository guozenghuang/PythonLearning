#九九乘法表

col = 1

while col <= 9 :

    row = 1

    while row <= col:
        result = row * col
        print(" %d * %d = %d ,"  % (row , col , result),end="")
        row = row + 1
    print("")

    col = col + 1