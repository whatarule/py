
from sys import stdin
from typing import Callable, List, Any
from builtins import map as _map
from functools import reduce as _reduce

def map(function) -> Callable[[list], list]:
  return lambda ls: list(_map(function, ls))
def reduce(function) -> Callable[[Any], Callable[[list], Any]]:
  return lambda acc: lambda ls: _reduce(function, ls, acc)
def compose(*functions) -> Callable[[Any], Any]:
  return _reduce(
      lambda f, g: lambda x: f(g(x))
    , functions
    , lambda x: x
    )

def intLs(int : int) -> List[int]:
  '''
  >>> intLs(15)
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  '''
  return [i + 1 for i in range(int)]

def fizzbuzz(int : int) -> str:
  '''
  >>> fizzbuzz(15)
  'Fizz Buzz'
  >>> fizzbuzz(3)
  'Fizz'
  >>> fizzbuzz(5)
  'Buzz'
  >>> fizzbuzz(1)
  '1'
  '''
  if int % 3 == 0 and int % 5 == 0:
    return "Fizz Buzz"
  elif int % 3 == 0:
    return "Fizz"
  elif int % 5 == 0:
    return "Buzz"
  else:
    return str(int)

def main():
  compose(
        map(print)
      , map(fizzbuzz)
      , intLs
      , int
      )(stdin.readline())
main()


