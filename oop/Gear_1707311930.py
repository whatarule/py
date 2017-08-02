
class Gear:
  def __init__(self
    , **args
    ) -> None:
    self._chaining = args["chaining"]
    self._cog = args["cog"]
    self._wheel = Wheel(args["rim"], args["tire"])

  def chaining(self) -> int:
    return self._chaining


  def ratio(self) -> float:
    '''
    >>> Gear(chaining=52,cog=11,rim=26,tire=1.5).ratio()
    4.7272727272727275
    '''
    return self._chaining / self._cog

  def gear_inches(self) -> float:
    '''
    >>> Gear(chaining=52,cog=11,rim=26,tire=1.5).gear_inches()
    137.0909090909091
    >>> Gear(chaining=52,cog=11,rim=24,tire=1.25).gear_inches()
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


