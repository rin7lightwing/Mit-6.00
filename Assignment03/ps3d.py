from string import find


def subStringMatchExact(target, key):
    """return a tuple of the starting points of matches of the key string in the target string"""
    ans = ()
    start = 0
    while find(target, key, start) != -1:
        start = find(target, key, start)
        ans += (start,)
        start += 1
    # print 'ans = ', ans
    return ans


def constrainedMatchPair(match1, match2, m):
    filtered = ()
    for n in match1:
        for k in match2:
            if n + m + 1 == k:
                filtered += (n,)
    return filtered


def subStringMatchOneSub(key, target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0, len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss + 1:]
        #print 'breaking key', key, 'into', key1, key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target, key1)
        match2 = subStringMatchExact(target, key2)
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
        # print 'match1', match1
        # print 'match2', match2
        #print 'possible matches for', key1, key2, 'start at', filtered
    return allAnswers


def subStringMatchExactlyOneSub(target, key):
    ans = subStringMatchExact(target, key)
    allAnswers = subStringMatchOneSub(key, target)
    oneSubAns = ()
    for aAns in allAnswers:
        if not ans.__contains__(aAns):
            oneSubAns += (aAns,)
    return oneSubAns


print subStringMatchExactlyOneSub('ATGACATGCACAAGTATGCAT', 'ATGC')


