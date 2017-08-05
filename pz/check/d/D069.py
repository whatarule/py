
from sys import stdin
from typing import Callable, List, Tuple, Any
from builtins import map as _map
from functools import reduce as _reduce

def map(function) -> Callable[[list], list]:
  return lambda ls: list(_map(function, ls))
def reduce(function) -> Callable[[Any], Callable[[list], Any]]:
  return lambda acc: lambda ls: _reduce(function, ls, acc)
def _(*functions) -> Callable[[Any], Any]:
  return _reduce(
      lambda f, g: lambda x: f(g(x))
    , functions
    , lambda x: x
    )
def _c2(f : Callable[[Any, Any], Any]) -> Callable[[Any], Callable[[Any], Any]]:
  return lambda x: lambda y: f(x,y)
def splitL(str : str) -> List[str]:
  return str.rstrip().split(" ")
def _add(x : int, y : int) -> int:
  return x + y
def add(x):
  return _c2(_add)(x)


def average(ls : List[int]) -> float:
  '''
  >>> average([50,40,50,60,30,80,100])
  58.57142857142857
  '''
  return reduce(_add)(0)(ls) / len(ls)

def _round(dec : int, x : float) -> float:
  return round(x, dec)

def main():
  _( print
  , _c2(_round)(1)
  , average
  , map(int)
  , splitL
  )(stdin.readline())
main()


