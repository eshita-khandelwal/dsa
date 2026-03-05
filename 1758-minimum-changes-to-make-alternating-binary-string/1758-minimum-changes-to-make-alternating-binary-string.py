class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        slist = list(s)
        for i in range(1,len(slist)):
            if slist[i-1]==slist[i]:
                res+=1
                if slist[i]=="1":
                    slist[i]="0"
                else:
                    slist[i]="1"
        res1 = 1
        slist2= list(s)
        if slist2[0]=="1":
            slist2[0]="0"
        else:
            slist2[0]="1"
        
        for i in range(1,len(slist2)):
            if slist2[i-1]==slist2[i]:
                res1+=1
                if slist2[i]=="1":
                    slist2[i]="0"
                else:
                    slist2[i]="1"
        return min(res,res1)

