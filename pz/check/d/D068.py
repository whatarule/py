
from sys import stdin
from typing import Callable, List, Tuple, Any
from builtins import map as _map
from functools import reduce as _reduce
from builtins import filter as _filter

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
def splitR(str : str) -> List[str]:
  return str.rstrip().split("\n")

def _con(s1 : str, s2 : str) -> str:
  return s1 + s2
def con(x):
  return _c2(_con)(x)
def conLs(ls : List[str]) -> str:
  return reduce(_con)("")(ls)
def conLsSp(ls : List[str]) -> str:
  if len(ls) == 0: return ""
  elif len(ls) == 1: return ls[0]
  else: return conLs([ls[0], " "]) +  conLsSp(ls[1:])

def sunny(w : str) -> bool:
  return w == "S"
def rainy(w : str) -> bool:
  return w == "R"

def _lsX(x : int, ls : List[Any]) -> Any:
  return ls[x]
def lsX(x):
  return _c2(_lsX)(x)

def filter(f : Callable[[Any], bool], ls : List[Any]) -> List[Any]:
  return _(list, _c2(_filter)(f))(ls)

def weatherD(s : str) -> List[int]:
  '''
  >>> weatherD("SSRSR")
  [3, 2]
  >>> weatherD("SSSSSSSSSS")
  [10, 0]
  >>> _(conLsSp, map(str))([3,2])
  "3 2"
  '''
  return [_(len, _c2(filter)(sunny))(s), _(len, _c2(filter)(rainy))(s)]

def main():
  _( print
  , conLsSp
  , map(str)
  , weatherD
  , lsX(1)
  , splitR
  )(stdin.read())
main()


