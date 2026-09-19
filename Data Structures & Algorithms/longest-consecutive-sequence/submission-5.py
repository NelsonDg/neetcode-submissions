class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                #check if its the start of sequence
                length = 1
                while (num + length) in numSet: #checks current number
                    length += 1
                longest = max(length, longest)
        return longest