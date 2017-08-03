
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

def tuple2(ls : List[Any]) -> Tuple[Any, Any]:
  '''
  >>> tuple2([1,1])
  (1, 1)
  >>> tuple2([0,99])
  (0, 99)
  '''
  return (ls[0], ls[1])
def _t2(f : Callable[[Any, Any], Any]) -> Callable[[Tuple[Any, Any]], Any]:
  return lambda ls: f(*ls)

def noEmpty(ls : List[str]) -> List[str]:
  '''
  >>> noEmpty(['10','','3','10000'])
  ['10', '3', '10000']
  '''
  return [x for x in ls if x != ""]
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

def _and(b1 : bool, b2 : bool) -> bool:
  '''
  >>> _and(True,True)
  True
  >>> _and(True,False)
  False
  >>> _and(False,False)
  False
  '''
  return b1 and b2
def _or(b1 : bool, b2 : bool) -> bool:
  '''
  >>> _or(True,True)
  True
  >>> _or(True,False)
  True
  >>> _or(False,False)
  False
  '''
  return b1 or b2
def _not(b : bool) -> bool:
  '''
  >>> _not(True)
  False
  >>> _not(False)
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
  return _c2(_add)(x)
def _sub(x : int, y : int) -> int:
  '''
  >>> sub(1)(3)
  -2
  >>> sub(0)(1)
  -1
  '''
  return x - y
def sub(x):
  return _c2(_sub)(x)
def _mult(x : int, y : int) -> int:
  '''
  >>> mult(0)(1)
  0
  >>> mult(2)(4)
  8
  '''
  return x * y
def mult(x):
  return _c2(_mult)(x)

def add_t(tpl):
  '''
  >>> add_t((0,1))
  1
  >>> add_t((1,3))
  4
  '''
  return _t2(_add)(tpl)

