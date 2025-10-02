from math import ceil

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink_bottles = numBottles
        while numBottles > 1:
            numBottles /= ceil(numExchange)
            drink_bottles += numBottles

        return int(drink_bottles)