# Write an iterative program that finds the largest number of McNuggets that cannot be bought in exact quantity.
# xa+yb+zc = n

def is_solvable(package):
    """package = (x, y, z), x<y<z"""
    x = int(package[0])
    y = int(package[1])
    z = int(package[-1])
    n = 0
    solutionExist = 0
    solutionNone = 0
    while solutionExist - solutionNone < x and n < 200:
        n += 1
        for a in range(0, n / x + 1):
            for b in range(0, n / y + 1):
                for c in range(0, n / z + 1):
                    if x * a + y * b + z * c == n:
                        solutionExist = n
                        # print a, b, c, '->', n
        if solutionExist != n:
            solutionNone = n
    print 'Largest number of McNuggets that cannot be bought in exact quantity: ', solutionNone

is_solvable((2, 6, 9))
