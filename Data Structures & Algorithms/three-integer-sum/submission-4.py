class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums): #enumerate acts like a counter
            if i > 0 and a == nums[i-1]: #check for duplicate
                continue
            l,r = i+1 , len(nums) -1   
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if(threeSum > 0): #if sum >0 r shifts left one
                    r-=1
                elif(threeSum < 0): #if sum < 0 l shifts right 1
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]]) #if they are equal
                    l+=1
                    while(nums[l] == nums[l-1]): 
                        l+=1
        return res