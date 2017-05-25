# -*- coding: utf-8 -*-

from typing import List

class OrOddEven:
  '''
  >>> OrOddEven(0).returnResult()
  'Even'
  >>> OrOddEven(1).returnResult()
  'Odd'
  >>> OrOddEven(0).printResult()
  Even: 0
  >>> OrOddEven(1).printResult()
  Odd: 1
  '''

  def __init__(self, i : int ) -> None:
    '''
    >>> OrOddEven(0).int
    0
    >>> OrOddEven(1).int
    1
    '''
    self.int = i

  def returnResult(self) -> str:
    if self.isOdd():
      str = 'Odd'
    elif self.isEven():
      str = 'Even'
    return str

  def printResult(self) -> None:
    print( '{0}: {1}'.format(
        self.returnResult()
      , self.int
      ))

  def isOdd(self) -> bool:
    '''
    >>> OrOddEven(0).isOdd()
    False
    >>> OrOddEven(1).isOdd()
    True
    '''
    if self.int % 2 == 1:
      return True
    else:
      return False

  def isEven(self) -> bool:
    '''
    >>> OrOddEven(0).isEven()
    True
    >>> OrOddEven(1).isEven()
    False
    '''
    if self.int % 2 == 0:
      return True
    else:
      return False


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
        lambda i: OrOddEven(i).returnResult()
      , self.intLs
      ))
  def printResult(self) -> None:
  # for i in self.intLs:
  #   OrOddEven(i).printResult()
    list(map (
        lambda i: OrOddEven(i).printResult()
      , self.intLs
      ))
  def isOdd(self) -> List[bool]:
    '''
    >>> list(map ( print, OrOddEvenLs(0,2).isOdd() ))
    False
    True
    [None, None]
    '''
    return list(map (
        lambda i: OrOddEven(i).isOdd()
      , self.intLs
      ))
  def isEven(self) -> List[bool]:
    '''
    >>> list(map ( print, OrOddEvenLs(0,2).isEven() ))
    True
    False
    [None, None]
    '''
    return list(map (
        lambda i: OrOddEven(i).isEven()
      , self.intLs
      ))


