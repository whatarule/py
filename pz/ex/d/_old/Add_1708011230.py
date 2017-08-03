# coding: utf-8

from functools import reduce

def pipe(x,*functions):
    return reduce(
          lambda f, g: lambda x: f(g(x))
        , functions
        , lambda x: x
        )(x)

def sum(ls):
    def add(x,y):
        return x+y
    return reduce(add, map(int, ls))

print(
    pipe(
      input()
        .rstrip()
        .split()
      , sum
      )
    )

