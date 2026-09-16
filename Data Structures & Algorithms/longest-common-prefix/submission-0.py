class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        n=len(strs)
        first=strs[0]
        last=strs[n-1]
        mn=min(len(first),len(last))
        cnt=0;
        for i in range(mn):
            if first[i]!=last[i]:
                break
            cnt+=1

        return first[:cnt]

        