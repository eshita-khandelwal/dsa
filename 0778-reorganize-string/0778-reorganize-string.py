class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = {}
        for i in range(len(s)):
            hashMap[s[i]] = 1 + hashMap.get(s[i],0)
        #use heap for this question, python by default uses minHeap so we have to use a hack here now
        maxHeap = [[-val,key] for key,val in hashMap.items()]
        heapq.heapify(maxHeap)

        ans = []

        while maxHeap:
            f,c = heappop(maxHeap)
            if not ans or c!=ans[-1]: #first char or not smae characters then input in ans
                ans.append(c)
                if f + 1!=0:
                    heappush(maxHeap,[f+1,c])
            else:
                if not maxHeap:
                    return ''
                f1,c1 = heappop(maxHeap)
                ans.append(c1)
                if f1+1!=0:
                    heappush(maxHeap,[f1+1,c1])
                heappush(maxHeap,[f,c])
        return "".join(ans)
                
            




        

