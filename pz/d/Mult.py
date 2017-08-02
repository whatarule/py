
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
  '''
  >>> splitR("1\\n1")
  ['1', '1']
  >>> splitR("0\\n99")
  ['0', '99']
  '''
  return str.rstrip().split("\n")

def mult(x : int, y : int) -> int:
  return x * y

def main():
  print( compose(
        reduce(mult)(1)
      , map(int)
      , splitR
      )(stdin.read())
    )
main()


