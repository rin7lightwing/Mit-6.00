# Write an iterative program that finds the largest number of McNuggets that cannot be bought in exact quantity.
# 6a+9b+20c = n

n = 0
solutionExist = 0
solutionNone = 0

while solutionExist - solutionNone < 6:
    n += 1
    for a in range(0, n / 6 + 1):
        for b in range(0, n / 9 + 1):
            for c in range(0, n / 20 + 1):
                if 6 * a + 9 * b + 20 * c == n:
                    # print a, b, c, '->', n
                    solutionExist = n
    if solutionExist != n:
        solutionNone = n
print 'Largest number of McNuggets that cannot be bought in exact quantity: ', solutionNone
