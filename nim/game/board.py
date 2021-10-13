import random
from typing import Text

class Board:

    def __init__(self) -> None:

        self.piles = []
        self._prepare()



    def to_string(self):

        text = '--------------------'
        for piles, stones in enumerate(self.piles):
            text += (f'\n {piles}: ' + ' O ' * stones)
        text += '\n--------------------'
        return text

    def apply(self,move):
        piles = move.get_pile()
        stones = move.get_stones()
        self.piles[piles] = max(0, self.piles[piles] - stones)

    def is_empty(self):
        
        empty = [0] * len(self.piles)
        return self.piles == empty

    def _prepare(self):
        piles = random.randint(2,5)
        for n in range(piles):
            stones = random.randint(1,9)
            self.piles.append(stones)
