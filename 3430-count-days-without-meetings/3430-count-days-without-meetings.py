class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings,key=lambda x:x[0])
        print(meetings)
        cnt=0
        for i in range(0,len(meetings)-1):
            if meetings[i][1]>=meetings[i+1][0]:
                if meetings[i][1]>=meetings[i+1][1]:
                    meetings[i+1][1] = meetings[i][1]
            else:
               cnt+=meetings[i+1][0] - meetings[i][1] -1 
        cnt+=meetings[0][0]-1
        cnt+=days-meetings[len(meetings)-1][1]
        
        return cnt