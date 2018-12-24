
def multiplication_table(n):
    l = [[0 for x in range(n)] for y in range(n)]
    print(l)
    for i in range(n):
        for j in range(n):
            l[i][j] = (i+1)*(j+1)
    return l

print(multiplication_table(10))

print(sum([i for i in range(100) if i % 3 == 0 or i % 10 == 0]))

l = [i for i in range(35)]