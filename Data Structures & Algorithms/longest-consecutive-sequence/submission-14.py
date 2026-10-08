class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
           if(num - 1) not in numSet: #checking the if its start of new sequence
                length = 1     
                while (num + length) in numSet: #check if its in sequence
                    length +=1
                    longest = max(longest,length) 
        return longest
