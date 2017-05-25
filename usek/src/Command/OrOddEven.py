# -*- coding: utf-8 -*-

from Odd import Odd
from Even import Even

from typing import List


class OrOddEven(Odd,Even):
  '''
  >>> OrOddEven(0).getStr()
  'Even'
  >>> OrOddEven(1).getStr()
  'Odd'
  >>> OrOddEven(0).printResult()
  Even: 0
  >>> OrOddEven(1).printResult()
  Odd: 1
  '''

  def __init__(self, i : int ) -> None:
    self.__val = i
    self._Even__val = i

  def getStr(self) -> str:
    if Odd(self.__val).returnResult():
      self.str = "Odd"
    elif self.isEven():
      self.str = "Even"
    return self.str

  def printResult(self) -> None:
    print( "{0}: {1}".format(
        self.getStr()
      , self.__val
      ))


class OrOddEvenLs:
  '''
  >>> list(map ( print, OrOddEvenLs(0,2).returnResult() ))
  Even
  Odd
  [None, None]
  >>> OrOddEvenLs(0,2).printResult()
  Even: 0
  Odd: 1
  '''
  def __init__(self,intS,intE) -> None:
    '''
    >>> list ( OrOddEvenLs(0,2).intLs )
    [0, 1]
    '''
    self.intLs = range(intS,intE)
  def returnResult(self) -> List[str]:
    return list(map (
        lambda i: OrOddEven(i).getStr()
      , self.intLs
      ))
  def printResult(self) -> None:
  # for i in self.intLs:
  #   OrOddEven(i).printResult()
    list(map (
        lambda i: OrOddEven(i).printResult()
      , self.intLs
      ))


