class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        store = {}
        for i in s:
            store[i] = store.get(i,0)+1
        
        if len(s)%2==0:
            for k,v in store.items():
                if v%2==1:
                    return False
            return True
        else:
            flag = 0
            for k,v in store.items():
                if v%2==1:
                    if flag==0:
                        flag=1
                    else:
                        return False
            return True


