from abc import ABC, abstractmethod


class Clothes(ABC):

    counter = 0

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, V):
        self.V = V

    @property
    def consumption(self):
        result = self.V/6.5 + 0.5
        Clothes.counter += round(result, 2)
        return round(result, 2)


class Suit(Clothes):

    def __init__(self, H):
        self.H = H

    @property
    def consumption(self):
        result = 2 * self.H + 0.3
        Clothes.counter += round(result, 2)
        return round(result, 2)


coat_1 = Coat(19)
print(coat_1.consumption)
suit_1 = Suit(7)
print(suit_1.consumption)
print(Clothes.counter)