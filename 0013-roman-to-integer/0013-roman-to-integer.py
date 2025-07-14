class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {}
        hashMap['I'] = 1
        hashMap['V'] = 5
        hashMap['X'] = 10
        hashMap['L'] = 50
        hashMap['C'] = 100
        hashMap['D'] = 500
        hashMap['M'] = 1000
        cnt = 0
        i =0
        while i<len(s):
            if i+1<len(s):
                if s[i] == 'I' and s[i+1] == 'V':
                    cnt+= 4
                    i+=2
                elif s[i] == 'I' and s[i+1] == 'X':
                    cnt+= 9
                    i+=2
                elif s[i] == 'X' and s[i+1] == 'L':
                    cnt+= 40
                    i+=2

                elif s[i] == 'X' and s[i+1] == 'C':
                    cnt+= 90
                    i+=2
                elif s[i] == 'C' and s[i+1] == 'D':
                    cnt+= 400
                    i+=2
                elif s[i] == 'C' and s[i+1] == 'M':
                    cnt+= 900
                    i+=2
                else:
                    cnt +=hashMap[s[i]]
                    i+=1

            else:    
                cnt +=hashMap[s[i]]
                i+=1
        return cnt
