# 1000th prime number

import math

odd = 5
count = 3

while count < 1000:
    odd += 2
    isPrime = True
    for divisor in range(2, int(math.sqrt(odd) + 1)):
        if odd % divisor == 0:
            isPrime = False
            break
    if isPrime:
        count += 1
print 'The 1000th prime number is', odd
