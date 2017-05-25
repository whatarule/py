# -*- coding: utf-8 -*-

from typing import List

class Odd:
  '''
  '''
  def __init__(self, i : int ) -> None:
    '''
    >>> Odd(0).val
    0
    >>> Odd(1).val
    1
    '''
    self.val = i

  def returnResult(self) -> bool:
    '''
    >>> Odd(0).returnResult
    False
    >>> Odd(1).returnResult
    True
    '''
    if self.val % 2 == 1:
      return True
    else:
      return False


