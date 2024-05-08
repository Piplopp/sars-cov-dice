from random import randint
from numbers import Number

class Die:
    """Simple dice.
    
    Attributes
    ----------
    sides: int
        Number of sides.
    name: str
        Dice name in the form of dx where x is the number of sides.
    """
    def __init__(self, x: int) -> None:
        if not isinstance(x, Number) or x <= 0:
            raise ValueError('Dice size can only be a non-zero positive integer.')
        self.name = 'd' + str(x)
        self.sides = x
    
    def __str__(self):
        return self.name

    def roll_once(self) -> int:
        return randint(1, self.sides)
    
    def roll_n(self, n: int) -> list[int]:
        if not isinstance(n, Number) or n <= 0:
            raise ValueError('Expected a non-zero positive integer')
        return [self.roll_once() for x in range(n)]
