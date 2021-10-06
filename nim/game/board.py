import random
from typing import Text

class Board:

    def __init__(self) -> None:

        self.piles = []
        self._prepare()



    def to_string(self):

        text = "----------------------------"
        for piles, stones in enumerate(self.piles):
            text += (f'\n{piles}:' + ' 0 ' * stones)
            text += "\n----------------------------"
            return text

    def apply(self,move):
       pile = move.get_pile()
       stone = move.get_stones()
       self.piles[pile] = max(0, self.piles[pile] - stone)

    def is_empty(self):
        if len(self.piles) == 0:
            return 1 == 1

    def _prepare(self):
        piles = random.randint(2,5)

        for x in range(piles):
            stones = random.randint(1,9)
            self.piles.append(stones)
