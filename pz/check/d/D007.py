
from sys import stdin
from typing import Callable, List, Tuple, Any
from functools import reduce as _reduce

def reduce(function) -> Callable[[Any], Callable[[list], Any]]:
  return lambda acc: lambda ls: _reduce(function, ls, acc)
def _(*functions) -> Callable[[Any], Any]:
  return _reduce(
      lambda f, g: lambda x: f(g(x))
    , functions
    , lambda x: x
    )

def multA(int : int) -> str:
  '''
  >>> multA(4)
  '****'
  >>> multA(6)
  '******'
  '''
  return "*" * int

def main():
  _( print
  , multA
  , int
  )(stdin.readline())
main()


