from string import find

def subStringMatchExact(target,key):
    """return a tuple of the starting points of matches of the key string in the target string"""
    ans = ()
    start = 0
    while find(target, key, start) != -1:
        start = find(target, key, start)
        ans += (start,)
        start += 1
    return ans

print subStringMatchExact("atgacatgcacaagtatgcat", "atgc")
# print subStringMatchExact('atgaatgcatggatgtaaatgcag', 'a')
