# -*- coding: utf-8 -*-

import Command
from Command import conLsSpaced
from typing import List


class Even:
  def __init__(self, val : int ) -> None:
    self.__val = val

  def isEven(self) -> bool:
    '''
    >>> Even(0).isEven()
    True
    >>> Even(1).isEven()
    False
    '''
    if self.__val % 2 == 0:
      return True
    else:
      return False

  def getEven(self) -> int:
    '''
    >>> Even(0).getEven()
    0
    >>> Even(1).getEven()
    Traceback (most recent call last):
    ...
    Exception: (Not even) 1
    '''
    if self.isEven():
      return self.__val
    else:
      try: raise Exception( conLsSpaced([
          "(Not even)"
        , str(self.__val)
        ]))
      except Exception:
        raise


