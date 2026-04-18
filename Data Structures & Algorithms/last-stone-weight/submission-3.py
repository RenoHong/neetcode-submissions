class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones) 
        while len(stones) > 1 :
            arr = stones[-2:]
            stones = stones[:-2]
            print(f"{arr} - >{stones} ")
            x = arr[0]
            y = arr[1] 

            if x != y :
                x = abs(x-y)
                stones.append(x)
            stones = sorted(stones)
        if stones:
            return stones[0]
        return 0