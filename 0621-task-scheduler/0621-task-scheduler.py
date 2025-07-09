class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #here we will use maxheap and queue, maxheap is to have the count of the most frq element so that we can start with it, and queue is for maintaing what is the next available task
        count = Counter(tasks) #creates a hasmap
        time = 0
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()

        while maxHeap or q:
            time +=1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt!=0:
                    q.append([cnt,time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time

