
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
def _c3(f : Callable[[Any, Any, Any], Any]) -> Callable[[Any], Callable[[Any], Callable[[Any], Any]]]:
  return lambda x: lambda y: lambda z: f(x,y,z)
def _c4(f):
  return lambda w: lambda x: lambda y: lambda z: f(w,x,y,z)

def splitR(str : str) -> List[str]:
  return str.rstrip().split("\n")
def splitL(str : str) -> List[str]:
  return str.rstrip().split(" ")

def _t(f):
  return lambda ls: f(*ls)
def tuple2(ls : List[Any]) -> Tuple[Any, Any]:
  return (ls[0], ls[1])
def _t2(f : Callable[[Any, Any], Any]) -> Callable[[Tuple[Any, Any]], Any]:
  return lambda ls: f(*ls)
def tuple3(ls : List[Any]) -> Tuple[Any, Any, Any]:
  return (ls[0], ls[1], ls[2])
def _t3(f : Callable[[Any, Any, Any], Any]) -> Callable[[Tuple[Any, Any, Any]], Any]:
  return lambda ls: f(*ls)
def tuple4(ls : List[Any]) -> Tuple[Any, Any, Any, Any]:
  return (ls[0], ls[1], ls[2], ls[3])
def _t4(f : Callable[[Any, Any, Any, Any], Any]) -> Callable[[Tuple[Any, Any, Any, Any]], Any]:
  return lambda ls: f(*ls)

def noEmpty(ls):
  return [x for x in ls if x != ""]
def nub(ls : list) -> list:
  if len(ls) < 2:
    return ls
  else:
    return [ls[0]] + nub([x for x in ls[1:] if x != ls[0]])
def intLs(int : int) -> List[int]:
  return [i + 1 for i in range(int)]

def _and(b1 : bool, b2 : bool) -> bool:
  return b1 and b2
def _or(b1 : bool, b2 : bool) -> bool:
  return b1 or b2
def _not(b : bool) -> bool:
  return not b

def _add(x : int, y : int) -> int:
  return x + y
def add(x):
  return _c2(_add)(x)
def _sub(x : int, y : int) -> int:
  return x - y
def sub(x):
  return _c2(_sub)(x)
def _mult(x : int, y : int) -> int:
  return x * y
def mult(x):
  return _c2(_mult)(x)


def main():
  _( print
  )(stdin.readline())
main()

