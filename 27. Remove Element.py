class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i , j = 0 , len(nums) - 1
        
        if len(nums) == 0:
            return 0
        k = 0
        
        while True:
            while j >= 0 and nums[j] == val:
                k +=1
                j -= 1        
            while i < len(nums)  and nums[i] != val:
                i+=1
            if i < j:
                nums[i] , nums[j] = nums[j] , nums[i]
                
            else:
                break
        
        
        return len(nums)  - k
                 
            
        
