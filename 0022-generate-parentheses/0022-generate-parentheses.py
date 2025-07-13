class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(o,c,s,n):
            nonlocal res
            if o == c == n:
                res.add(s)
                return
            if o<=n:
                generate(o+1,c,s+'(',n)
            if c<o:
                generate(o,c+1,s+')',n)

        res = set()
        generate(0,0,'',n)
        return list(res)