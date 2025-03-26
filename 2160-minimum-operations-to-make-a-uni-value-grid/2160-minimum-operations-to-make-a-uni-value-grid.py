class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        comp = []
        t = grid[0][0]%2
        for row in grid:
            for num in row:
                comp.append(num)
        comp = sorted(comp)
        n = len(comp)
        ans = 0
        if n%2==0 and n>2:
            cnt1 = 0
            m1 = comp[n//2]
            for num in comp:
                modv = abs(num-m1)% x
                if modv!=0:
                    break
                cnt1+=abs(num-m1)//x
            cnt2=0
            m2 = comp[(n//2)+1]
            for num in comp:
                modv = abs(num-m1)% x
                if modv!=0:
                    return -1
                cnt2+=abs(num-m2)//x
            return min(cnt1,cnt2)
        
        m1 = comp[n//2]
        for num in comp:
            modv = abs(num-m1)% x
            if modv!=0:
                return -1
            ans+=abs(num-m1)//x
        return ans



