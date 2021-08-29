class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horCuts = [0] + sorted(horizontalCuts) + [h]
        vertCuts = [0] + sorted(verticalCuts) + [w]
        
        maxX = 0
        for i in range(len(horCuts) - 1):
            size = horCuts[i + 1] - horCuts[i]
            if size > maxX:
                maxX = size
        
        maxY = 0
        for i in range(len(vertCuts) - 1):
            size = vertCuts[i + 1] - vertCuts[i]
            if size > maxY:
                maxY = size
                
                
        return (maxY * maxX)  % ((10 ** 9) + 7)