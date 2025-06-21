class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result+=str(len(s))
            result+='#'
            result+=s
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i =0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            l = int(s[i:j])
            strs.append(s[j+1:j+1+l])
            i = j+1+l
        return strs
        


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))