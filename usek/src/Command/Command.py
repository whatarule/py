# -*- coding: utf-8 -*-

from typing import List
from functools import reduce

def conLsSeparated(
  spr : str, strLs : List[str]
  ) -> str:
  '''
  >>> conLsSeparated( " ", ["aaa","bbb","ccc"] )
  'aaa bbb ccc'
  >>> conLsSeparated( ",", ["aaa","bbb","ccc"] )
  'aaa,bbb,ccc'
  >>> conLsSeparated( ", ", ["aaa","bbb","ccc"] )
  'aaa, bbb, ccc'
  '''
  return reduce (
      lambda acc, str: acc + spr + str
    , strLs, ""
    ) [len(spr):]

def conLsSpaced( strLs : List[str] ) -> str:
  '''
  >>> conLsSpaced(["aaa","bbb","ccc"])
  'aaa bbb ccc'
  '''
  return conLsSeparated( " ", strLs )


