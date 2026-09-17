class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            if nums[i]!=val:
                nums[cnt]=nums[i]
                cnt+=1


        return cnt
        