
from sys import stdin
from typing import Callable, List, Any
from builtins import map as _map
from functools import reduce as _reduce

def map(function) -> Callable[[list], list]:
  return lambda ls: list(_map(function, ls))
def reduce(function) -> Callable[[Any], Callable[[list], Any]]:
  return lambda acc: lambda ls: _reduce(function, ls, acc)
def compose(*functions) -> Callable[[Any], Any]:
  return _reduce(
      lambda f, g: lambda x: f(g(x))
    , functions
    , lambda x: x
    )

def splitR(str : str) -> List[str]:
  return str.rstrip().split("\n")

def sort(ls : List[int]) -> List[int]:
  if ls == []:
    return []
  else:
    lsSmaller = [x for x in ls[1:] if x <= ls[0] ]
    lsLarger = [x for x in ls[1:] if x > ls[0] ]
    return sort(lsSmaller) + [ls[0]] + sort(lsLarger)

def main():
  print( compose(
        sort
      , map(int)
      , splitR
      )(stdin.read())
    )
main()


