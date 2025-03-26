class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(" ")
        if arr[0][0]!=arr[len(arr)-1][len(arr[len(arr)-1])-1]:
            return False
        prev = arr[0][len(arr[0])-1]
        for i in range(1,len(arr)):
            if arr[i][0]!=prev:
                return False
            prev = arr[i][len(arr[i])-1]
        return True

