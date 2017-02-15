# Write two functions, called countSubStringMatch and countSubStringMatchRecursive that take two arguments, a key string and a target string. These functions iteratively and recursively count the number of instances of the key in the target string.

from string import find


def countSubStringMatch(target, key):
    """Count the number of times that a key string appears in a target string."""
    count = 0
    start = 0
    while find(target, key, start) != -1:
        start = find(target, key, start) + 1
        count += 1
    return count


def countSubStringMatchRecursive(target, key):
    """Count the number of times that a key string appears in a target string."""
    count = 0
    while len(target) >= len(key):
        start = find(target, key) + 1
        if start != 0:
            count += 1
            target = target[start:]
        else:
            break
    return count

# print countSubStringMatch('atgacatgcacaagtatgcat', 'atgc')
# print countSubStringMatchRecursive('atgacatgcacaagtatgcat', 'atgc')
