class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def checkCuts(rectangles,dim)->bool:
            gapCount=0
            rectangles = sorted(rectangles,key=lambda x:x[dim])
            furthestEnd = rectangles[0][dim+2]
            print(rectangles)
            for i in range(1,len(rectangles)):
                if furthestEnd<=rectangles[i][dim]:
                    gapCount+=1
                furthestEnd=max(furthestEnd,rectangles[i][dim+2])
            
            return gapCount>=2
        
        return checkCuts(rectangles,0) or checkCuts(rectangles,1)

        