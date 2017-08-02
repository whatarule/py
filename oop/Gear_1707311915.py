
class Gear:
  def __init__(self
    , chaining : int
    , cog : int
    , rim : int
    , tire : float
    ) -> None:
    self._chaining = chaining
    self._cog = cog
    self._wheel = Wheel(rim, tire)

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
    return self.ratio() * self._wheel.diameter()

class Wheel:
  def __init__(self
      , rim : int
      , tire : float
      ) -> None:
    self._rim = rim
    self._tire = tire

  def diameter(self) -> float:
    return self._rim + (self._tire * 2)


