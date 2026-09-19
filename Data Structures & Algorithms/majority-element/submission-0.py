class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        n=len(nums)
        cand=nums[0]

        for i in nums:
            if cnt==0:
                cand=i
                cnt+=1
            elif cand==i :
                cnt+=1
            else :
                cnt-=1

        return cand