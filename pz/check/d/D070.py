
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

def splitL(str : str) -> List[str]:
  return str.rstrip().split(" ")
def tuple2(ls : List[int]) -> Tuple[int, int]:
  return (ls[0], ls[1])
def _t2(f : Callable[[Any, Any], Any]) -> Callable[[Tuple[Any, Any]], Any]:
  return lambda ls: f(*ls)
def _sub(x : int, y : int) -> int:
  return x - y

def main():
  _( print
  , _(_t2(_sub), tuple2)
  , map(int)
  , splitL
  )(stdin.readline())
main()


