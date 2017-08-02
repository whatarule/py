
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

def splitL(str : str) -> List[str]:
  '''
  >>> splitL("1 1")
  ['1', '1']
  >>> splitL("0 99")
  ['0', '99']
  '''
  return str.rstrip().split(" ")

def add(x : int, y : int) -> int:
  return x + y

def main():
  print( compose(
        reduce(add)(0)
      , map(int)
      , splitL
      )(stdin.readline())
    )
main()


