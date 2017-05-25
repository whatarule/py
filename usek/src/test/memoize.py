
def memoize(f):
    cache = {}
    def helper(x,y):
        if (x,y) not in cache:
            cache[(x,y)] = f(x,y)
        return cache[(x,y)]
    return helper


