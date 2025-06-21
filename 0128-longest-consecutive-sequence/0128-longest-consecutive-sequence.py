class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set()
        # for n in nums:
        #     numSet.add(n)
        # longest = 0

        # for n in nums:
        #     if n-1 not in numSet:
        #         length = 0
        #         while n+length in numSet:
        #             length+=1
        #         longest = max(longest,length)
        # return longest
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                # current_num = num
                # current_streak = 1
                length = 0
                while num + length in num_set:
                    # current_num += 1
                    # current_streak += 1
                    length+=1

                longest_streak = max(longest_streak,length)

        return longest_streak