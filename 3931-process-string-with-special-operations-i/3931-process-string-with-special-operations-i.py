class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for c in s:
            if c!='#' and c!='*' and c!='%':
                res+=c
            else:
                if c=='#':
                    if res:
                        res+=res
                elif c == '%':
                    if res:
                        res = res[::-1]
                elif c == '*':
                    if res:
                        res = res[:len(res)-1]
        return res