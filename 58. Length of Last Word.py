class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split(" ")
        
        l = len(st) - 1
        
        while len(st[l]) == 0:
            l-=1
            
        return len(st[l])
