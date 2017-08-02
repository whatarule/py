
class Gear:
  def __init__(self, chaining : int, cog : int) -> None:
    '''
    >>> Gear(52,11)._chaining
    52
    >>> Gear(52,11)._cog
    11
    '''
    self._chaining = chaining
    self._cog = cog

  def ratio(self) -> float:
    '''
    >>> Gear(52,11).ratio()
    4.7272727272727275
    >>> Gear(30,27).ratio()
    1.1111111111111112
    '''
    return self._chaining / self._cog



