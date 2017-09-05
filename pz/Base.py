
from sys import stdin
from typing import Callable, List, Tuple, Any
from functools import reduce as reduce_
from builtins import map as map_
from functools import wraps, partial
from builtins import (
    filter as filter_
  , zip as zip_
  , round as round_
  )
from math import floor, ceil

def identity(x : Any) -> Any: return x
def reduce(function) -> Callable[[Any], Callable[[list], Any]]:
  return lambda acc: lambda ls: reduce_(function, ls, acc)
def compose2(f, g): return lambda *args: f(g(*args))
def _(*functions) -> Callable[[Any], Any]:
  return reduce_(compose2, functions, identity)
def map(*functions) -> Callable[[list], list]:
  return lambda ls: list(map_(_(*functions), ls))
def _t(f): return lambda ls: f(*ls)
def _c2(f : Callable[[Any, Any], Any]) -> Callable[[Any], Callable[[Any], Any]]:
  return lambda x: lambda y: f(x, y)
def _l2(f : Callable[[Any], Any], g : Callable[[Any], Any]) -> Callable[[Any], Tuple[Any, Any]]:
  return lambda x: (f(x), g(x))

def curry(f):
  @wraps(f)
  def curried(*args, **kwargs):
    if len(args) == f.__code__.co_argcount:
      return f(*args)
    elif len(args) == f.__code__.co_argcount - 1:
      return partial(f, *args)
    elif len(args) == f.__code__.co_argcount - 2:
      return _t(partial(f, *args))
    else:
      def _f(*_xs, **_ks):
        return partial(f, *args)(*_xs)
      return curry(_f)
  return curried

def _f2(f : Callable[[Any, Any], Any]) -> Callable[[Any], Callable [[Any], Any]]:
  def _f(y,x): return f(x,y)
  return curry(_f)
def _f3(f):
  def _f(y, z, x): return f(x, y, z)
  return curry(_f)
def _f3_2(f): return _(_f3, _f3)(f)

def rstrip(s : str) -> str: return s.rstrip()
@curry
def split(spl : str, s : str) -> List[str]:
  return s.split(spl)
def splitR(s : str) -> List[str]:
  return _(split("\n"), rstrip)(s)
def splitL(s : str) -> List[str]:
  return _(split(" "), rstrip)(s)
def noEmpty(ls : List[str]) -> List[str]:
  return [x for x in ls if x != ""]
@curry
def pop(i : int, ls : list) -> list:
  ls.pop(i)
  return ls

@curry
def filter(f : Callable[[Any], bool], ls : List[Any]) -> List[Any]:
  return _(list, _c2(filter_)(f))(ls)
@curry
def eq(x : Any, y : Any) -> bool: return x == y
@curry
def eqT(i : int, tp1 : tuple, tp2 : tuple) -> bool:
  return tp1[i] == tp2[i]

@curry
def lsX(i : int, ls : list) -> Any: return ls[i]
@curry
def tpX(i : int ,tp : tuple) -> Any: return tp[i]
@curry
def zip(ls1 : list, ls2 : list):
  return list(zip_(ls1, ls2))
def intLs(int : int) -> List[int]:
  return [i + 1 for i in range(int)]

def tail(ls : list) -> list: return ls[1:]
def init(ls : list) -> list: return ls[:len(ls)-1]
def last(ls : list) -> Any: return ls[len(ls)-1]

def nub(ls : list) -> list:
  if len(ls) < 2:
    return ls
  else:
    return [ls[0]] + nub([x for x in ls[1:] if x != ls[0]])
@curry
def set(ls : list, i : int, x : Any) -> list:
  ls[i] = x
  return ls
@curry
def insert(i : int, x : Any, ls : list) -> list:
  ls.insert(i, x)
  return ls
@curry
def addLs(ls1 : list, ls2 : list) -> list: return ls1 + ls2
def reverse(ls : list) -> list:
  ls.reverse()
  return ls

@curry
def sort(f : Callable[[Any, Any], bool], ls : List[int]) -> List[int]:
  if ls == []:
    return []
  else:
    lsSmaller = [x for x in ls[1:] if f(x, ls[0]) ]
    lsLarger = [x for x in ls[1:] if not f(x, ls[0]) ]
    return sort(f)(lsSmaller) + [ls[0]] + sort(f)(lsLarger)
@curry
def gt(x : Any, y : Any) -> bool: return x > y
@curry
def lt(x : Any, y : Any) -> bool: return x < y

@curry
def gtLs(i : int, ls1 : list, ls2 : list): return ls1[i] > ls2[i]
@curry
def ltLs(i : int, ls1 : list, ls2 : list): return ls1[i] < ls2[i]
@curry
def gtT(i : int, t1 : tuple, t2 : tuple): return t1[i] > t2[i]
@curry
def ltT(i : int, t1 : tuple, t2 : tuple): return t1[i] < t2[i]

@curry
def replace(old : str, new : str, s : str) -> str:
  return s.replace(old, new)
@curry
def con(s1 : str, s2 : str) -> str:
  return s1 + s2
def conLs(ls : List[str]) -> str:
  return reduce(con)("")(ls)
@curry
def conLsSep(sep : str, ls : List[str]) -> str:
  if len(ls) == 0: return ""
  elif len(ls) == 1: return ls[0]
  else: return conLs([ls[0], sep]) +  conLsSep(sep, ls[1:])
def conLsSp(ls : List[str]) -> str:
  return conLsSep(" ", ls)

def _not(b : bool) -> bool: return not b
@curry
def _and(b1 : bool, b2 : bool) -> bool: return b1 and b2
@curry
def _or(b1 : bool, b2 : bool) -> bool: return b1 or b2

@curry
def any(f,ls): return _(reduce(_or)(False), map(f))(ls)
@curry
def all(f,ls): return _(reduce(_and)(True), map(f))(ls)

def neg(x): return x * (-1)
@curry
def add(x, y): return x + y
@curry
def sub(x, y): return x - y
@curry
def mlt(x, y): return x * y
@curry
def div(x, y): return x / y
@curry
def mod(x, y): return x % y

def digit2(i : int) -> str:
  s = str(i)
  d = _(len, str)(i)
  if d == 1: return "0" + s
  else: return s
def digit3(i : int) -> str:
  s = str(i)
  d = _(len, str)(i)
  if d == 1: return "00" + s
  elif d == 2: return "0" + s
  else: return s
def average(ls : List[int]) -> float:
  return reduce(add)(0)(ls) / len(ls)
@curry
def round(dec : int, x : float) -> float:
  return round_(x, dec)
def hundred(i : int) -> int:
  return _(floor, _f2(div)(100))(i) % 100





def main():
  _(identity
  , map(print)

  , noEmpty
  , splitL
  , rstrip
  )(stdin.readline())
main()

