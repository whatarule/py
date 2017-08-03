
from sys import stdin
from typing import List
from builtins import map as _map
from functools import reduce as _reduce


def _pipe(x, *functions):
  return _reduce(
      lambda f, g: lambda x: g(f(x))
    , functions
    , lambda x: x
    )(x)
def pipe(x):
  return lambda *functions: pipe(x, *functions)

def map(function):
  return lambda ls: _map(function, ls)
def reduce(function):
  return lambda acc: lambda ls: _reduce(function, ls, acc)
def compose(*functions):
  return _reduce(
      lambda f, g: lambda x: f(g(x))
    , functions
    , lambda x: x
    )

def splitR(str : str) -> List[str]:
  '''
  >>> splitR("1\\n1")
  ['1', '1']
  >>> splitR("0\\n99")
  ['0', '99']
  '''
  return str.rstrip().split("\n")

def mult(x : int, y : int) -> int:
  return x * y

def main():
  print( compose(
        reduce(mult)(1)
      , map(int)
      , splitR
      )(stdin.read())
    )
main()


