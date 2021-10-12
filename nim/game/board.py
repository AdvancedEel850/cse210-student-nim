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
        for i in range(self.piles):
            if i == move.get_pile():
                self.piles[i] = max(0, self.piles[i] - move.get_stones())
            else:
                pass

    def is_empty(self):
        if len(self.piles) == 0:
            return 1 == 1

    def _prepare(self):
        piles = random.randint(2,5)

        for x in range(piles):
            stones = random.randint(1,9)
            self.piles.append(stones)
