def commonPrefix(s1,s2):
    res = ""
    
    for i in range(min([len(s1),len(s2)])):
        if s1[i] != s2[i]:
            break
        else:
            res+=s1[i]
        
    return res
        
    
    
def lcs(strs,low, high):
    if low < high:
        mid = low + (high - low)//2
        
        s1 = lcs(strs,low,mid)
        s2 = lcs(strs,mid+1,high)
        
        return commonPrefix(s1,s2)
    else:
        return strs[low]




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return lcs(strs,0,len(strs) - 1)
                
                
