class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        cnt=0
        arr=[]
        for i in nums:
            if i!=val:
                arr.append(i)
                cnt+=1
        for i in range(len(arr)):
            nums[i]=arr[i]

        return cnt
        