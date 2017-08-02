
class Gear:
  def __init__(self
    , chaining : int
    , cog : int
    , wheel
    ) -> None:
    self.__chaining = chaining
    self.__cog = cog
    self.__wheel = wheel

  def ratio(self) -> float:
    '''
    >>> Gear(52,11,Wheel(26,1.5)).ratio()
    4.7272727272727275
    '''
    return self.__chaining / self.__cog

  def gear_inches(self) -> float:
    '''
    >>> Gear(52,11,Wheel(26,1.5)).gear_inches()
    137.0909090909091
    >>> Gear(52,11,Wheel(24,1.25)).gear_inches()
    125.27272727272728
    '''
    return self.ratio() * self.__wheel.diameter()

class Wheel:
  def __init__(self
      , rim : int
      , tire : float
      ) -> None:
    self.__rim = rim
    self.__tire = tire

  def diameter(self) -> float:
    return self.__rim + (self.__tire * 2)


