class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {}
        total = 0
        for i in stones:
            hashmap[i] = stones.count(i)

        print(hashmap)
        for jewel in jewels:
            total += (0 if jewel not in  hashmap else hashmap[jewel])

        return total