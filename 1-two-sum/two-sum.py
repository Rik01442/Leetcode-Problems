class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydictionary={}
        for index,element in enumerate(nums):
            mydictionary[element]=index
        
        for index,x in enumerate(nums):
            y=target-x
            if y in mydictionary and mydictionary[y]!=index:
                return([index,mydictionary[y]])

            


