
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

def splitR(str : str) -> List[str]:
  return str.rstrip().split("\n")
def splitL(str : str) -> List[str]:
  return str.rstrip().split(" ")

def intLs(int : int) -> List[int]:
  return [i + 1 for i in range(int)]

def tuple2(ls : List[int]) -> Tuple[int, int]:
  return (ls[0], ls[1])

def _toGroup(seat : int, n : int) -> List[int]:
  '''
  >>> toGroup(6)(3)
  [6, 7, 8]
  '''
  return [x + seat for x in range(n)]
def toGroup(seat):
  return lambda n: _toGroup(seat, n)
def toGroup_t2(tpl):
  return _toGroup(*tpl)

def _and(b1 : bool, b2 : bool) -> bool:
  return b1 and b2

def _unseated(ls : List[int], cst : int) -> bool:
  '''
  >>> unseated([0,1])(2)
  True
  >>> unseated([0,1])(1)
  False
  '''
  return reduce(_and)(True)(map(lambda i: i != cst)(ls))
def unseated(ls):
  return lambda cst: _unseated(ls, cst)

def _addCustomer(lsS : List[int], lsC : List[int]) -> List[int]:
  '''
  >>> addCustomer([1,2])([3,4])
  [1, 2, 3, 4]
  >>> addCustomer([0,1])([0,1])
  [0, 1]
  >>> addCustomer([0,1])([0,2])
  [0, 1]
  '''
  if reduce(_and)(True)(map(unseated(lsS))(lsC)):
    return lsS + lsC
  else:
    return lsS
def addCustomer(ls):
  return lambda cst: _addCustomer(ls, cst)

def main():
  _( print
  , len
  , reduce(_addCustomer)([])
  , map(_(toGroup_t2, tuple2))
  , map(map(int))
  , map(splitL)
  , splitR
  )(stdin.read())
main()


