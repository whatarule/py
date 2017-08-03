
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
  return lambda x: lambda y: f(x, y)
def _t2(f : Callable[[Any, Any], Any]) -> Callable[[Tuple[Any, Any]], Any]:
  return lambda ls: f(*ls)


def splitR(str : str) -> List[str]:
  '''
  >>> splitR("1\\n1")
  ['1', '1']
  >>> splitR("0\\n99")
  ['0', '99']
  '''
  return str.rstrip().split("\n")
def splitL(str : str) -> List[str]:
  '''
  >>> splitL("1 1")
  ['1', '1']
  >>> splitL("0 99")
  ['0', '99']
  '''
  return str.rstrip().split(" ")

def nub(ls : list) -> list:
  '''
  >>> nub(['red','green','blue','blue','green','blue'])
  ['red', 'green', 'blue']
  >>> nub(['Nagato','Yukikaze','Akagi','Kitakami','Nagato','Akagi','Akagi','Kitakami'])
  ['Nagato', 'Yukikaze', 'Akagi', 'Kitakami']
  '''
  if len(ls) < 2:
    return ls
  else:
    return [ls[0]] + nub([x for x in ls[1:] if x != ls[0]])
def intLs(int : int) -> List[int]:
  '''
  >>> intLs(15)
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  '''
  return [i + 1 for i in range(int)]
def tuple2(ls : List[int]) -> Tuple[int, int]:
  return (ls[0], ls[1])

def _and(b1 : bool, b2 : bool) -> bool:
  '''
  >>> _c2(_and)(True)(True)
  True
  >>> and_(True)(False)
  False
  >>> and_(False)(False)
  False
  '''
  return b1 and b2
def and_(b1):
  return lambda b2: _and(b1, b2)
def _or(b1 : bool, b2 : bool) -> bool:
  '''
  >>> or_(True)(True)
  True
  >>> or_(True)(False)
  True
  >>> or_(False)(False)
  False
  '''
  return b1 or b2
def or_(b1):
  return lambda b2: _or(b1, b2)
def not_(b : bool) -> bool:
  '''
  >>> not_(True)
  False
  >>> not_(False)
  True
  '''
  return not b

def _add(x : int, y : int) -> int:
  '''
  >>> add(0)(1)
  1
  >>> add(1)(3)
  4
  '''
  return x + y
def add(x):
  return lambda y: _add(x, y)
def _mult(x : int, y : int) -> int:
  '''
  >>> mult(0)(1)
  0
  >>> mult(2)(4)
  8
  '''
  return x * y
def mult(x):
  return lambda y: _mult(x, y)


