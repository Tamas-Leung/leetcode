class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypesSorted = sorted(boxTypes, key = lambda x: int(x[1]), reverse=True)
        
        sizeLeft = truckSize
        unitTotal = 0
        
        for boxType in boxTypesSorted:
            unitTotal += boxType[0] * boxType[1]
            sizeLeft -= boxType[0]
            if sizeLeft <= 0:
                unitTotal += sizeLeft*boxType[1]
                break
                
        return unitTotal