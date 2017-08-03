
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
def not_(b : bool) -> bool:
  return not b

def checkT(t : int) -> bool:
  '''
  >>> checkT(25)
  True
  >>> checkT(24)
  False
  '''
  if t < 25:
    return False
  else:
    return True

def checkH(h : int) -> bool:
  '''
  >>> checkH(40)
  True
  >>> checkH(41)
  False
  '''
  if h > 40:
    return False
  else:
    return True

def _checkL_or(t, h):
  return checkT(t) or checkH(h)
def __checkL_and(t, h):
  return checkT(t) and checkH(h)
def _checkL_and(tpl):
  return __checkL_and(*tpl)
def _checkL(t : int, h : int) -> str:
  '''
  >>> checkL((25,50))
  'Yes'
  >>> checkL((10,20))
  'Yes'
  >>> checkL((20,50))
  'No'
  '''
  if _checkL_or(t,h) and _(not_, _checkL_and)((t, h)):
    return "Yes"
  else:
    return "No"
def checkL(tpl):
  return _checkL(*tpl)

def main():
  _( print
    , _(checkL, tuple2)
    , map(int)
    , splitL
  )(stdin.readline())
main()


