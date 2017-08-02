
class Gear:
  def __init__(self
    , chaining : int
    , cog : int
    , rim : int
    , tire : float
    ) -> None:
    '''
    >>> Gear(52,11,26,1.5)._chaining
    52
    >>> Gear(52,11,26,1.5)._cog
    11
    >>> Gear(52,11,26,1.5)._rim
    26
    >>> Gear(52,11,26,1.5)._tire
    1.5
    '''
    self._chaining = chaining
    self._cog = cog
    self._rim = rim
    self._tire = tire

  def ratio(self) -> float:
    '''
    >>> Gear(52,11,26,1.5).ratio()
    4.7272727272727275
    '''
    return self._chaining / self._cog

  def gear_inches(self) -> float:
    '''
    >>> Gear(52,11,26,1.5).gear_inches()
    137.0909090909091
    >>> Gear(52,11,24,1.25).gear_inches()
    125.27272727272728
    '''
    return self.ratio() * (self._rim + (self._tire *2))


