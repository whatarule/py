# coding: utf-8

from functools import reduce

def pipe(x,*functions):
    return reduce(
          lambda f, g: lambda x: f(g(x))
        , functions
        , lambda x: x
        )(x)

def inputLines():
    ls = []
    for i in range(int(input())):
        ls.append(input().rstrip())
    ls = list(map(int, ls))
    return ls

def quicksort(ls):
    #ls.sort()
    #return ls
    if ls == []:
        return []
    else:
        lsSmaller = [x for x in ls[1:] if x <= ls[0] ]
        lsLarger = [x for x in ls[1:] if x > ls[0] ]
        return quicksort(lsSmaller) + [ls[0]] + quicksort(lsLarger)

def printLs(ls):
    for i in range(len(ls)):
        print(ls[i])

printLs(
    pipe(
        inputLines()
        , quicksort
        )
    )
