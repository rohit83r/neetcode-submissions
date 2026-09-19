class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr=strs
        ans={}
        for i in strs:
            sorted_string=''.join(sorted(i))
            if sorted_string not in ans:
                ans[sorted_string]=[]
            ans[sorted_string].append(i)


        res=[]
        for value in ans.values():
            res.append(value)

        return res

        