class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                total_sum = nums[i] + nums[start] + nums[end]
                
                if abs(total_sum - target) < abs(diff):
                    diff = total_sum - target
                
                if total_sum < target:
                    start += 1
                else:
                    end -= 1
        
        return target + diff
