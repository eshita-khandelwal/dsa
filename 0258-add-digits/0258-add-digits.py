class Solution:
    def addDigits(self, num: int) -> int:
        cnt = 0
        while num > 9:
            res = []
            while num > 0:
                res.append(num%10)
                num = num //10
            i = 0
            
            while i<len(res):
                num+=res[i]
                i+=1

        return num
            
