
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
def _c3(f : Callable[[Any, Any, Any], Any]) -> Callable[[Any], Callable[[Any], Callable[[Any], Any]]]:
  return lambda x: lambda y: lambda z: f(x, y, z)
def splitL(str : str) -> List[str]:
  return str.rstrip().split(" ")
def tuple3(ls : List[Any]) -> Tuple[Any, Any, Any]:
  return (ls[0], ls[1], ls[2])
def _t3(f : Callable[[Any, Any, Any], Any]) -> Callable[[Tuple[Any, Any, Any]], Any]:
  return lambda ls: f(*ls)
def intLs(int : int) -> List[int]:
  return [i + 1 for i in range(int)]
def noEmpty(ls):
  return [x for x in ls if x != ""]

def _checkV(data : int, vol : int, qt : int) -> bool:
  '''
  >>> checkV(10)(3)(4)
  True
  >>> checkV(10)(3)(3)
  False
  '''
  return not(data > vol * qt)
def checkV(x):
  return _c3(_checkV)(x)

def _culcQ(data : int, vol : int) -> int:
  '''
  >>> _culcQ(10,3)
  4
  >>> _culcQ(3,3)
  1
  '''
  lsB = map(checkV(data)(vol))(intLs(1000))
  return len([x for x in lsB if x == False]) + 1

def _culcP(data : int, vol : int, yen : int) -> int:
  '''
  >>> culcP((10,3,10000))
  40000
  >>> culcP((3,3,2500))
  2500
  '''
  return yen * _culcQ(data, vol)
def culcP(tpl):
  return _t3(_culcP)(tpl)

def main():
  _( print
  , culcP
  , map(int)
  , noEmpty
  , splitL
  )(stdin.readline())
main()


