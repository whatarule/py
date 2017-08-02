
from sys import stdin
from typing import Callable, List, Any
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
# def nub_0(ls, x):
#   if ls.count(x) == 0:
#     return ls + [x]
#   else:
#     return ls
# return reduce(nub_0)([])(ls)

def _countInLs(ls : list, x : Any) -> int:
  '''
  >>> countInLs(['red','green','blue','blue','green','blue'])('red')
  1
  >>> countInLs(['Nagato','Yukikaze','Akagi','Kitakami','Nagato','Akagi','Akagi','Kitakami'])('Nagato')
  2
  '''
  return len([y for y in ls if y == x])
def countInLs(ls):
  return lambda x: _countInLs(ls, x)

def _map2(f : Callable[[list], Callable[[Any], Any]], ls : list) -> list:
  '''
  >>> map2(countInLs)(['red','red','blue'])
  [2, 2, 1]
  '''
  return map(f(ls))(ls)
def map2(f):
  return lambda ls: _map2(f, ls)

def _conF(f : Callable[[Any], Any], string : str) -> str:
  '''
  >>> conF(countInLs(['red','green','blue','blue','green','blue']))('red')
  'red 1'
  >>> conF(countInLs(['Nagato','Yukikaze','Akagi','Kitakami','Nagato','Akagi','Akagi','Kitakami']))('Nagato')
  'Nagato 2'
  '''
  return string + " " + _(str, f)(string)
def conF(f):
  return lambda string: _conF(f, string)


def main():
  _( map(print)
  , lambda ls: map(conF(countInLs(ls)))(nub(ls))
  , splitL
  )(stdin.readline())
main()


