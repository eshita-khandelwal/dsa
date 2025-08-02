class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_starting = [float("-inf")] * n
        prefix_ending = [float("-inf")] * n
        prefix_starting[0] = arr[0]
        prefix_ending[n-1] = arr[n-1]

        for i in range(1,n):
            prefix_starting[i] = max(prefix_starting[i-1] + arr[i],arr[i])
        for i in range(n-2,-1,-1):
            prefix_ending[i] = max(prefix_ending[i+1]+arr[i],arr[i])
        print(prefix_starting,prefix_ending)
        max_without_deletion = max(prefix_starting)
        max_with_deletion = float("-inf")
        for i in range(1,n-1):
            max_with_deletion = max(max_with_deletion,prefix_starting[i-1] + prefix_ending[i+1])
        return max(max_with_deletion,max_without_deletion)
