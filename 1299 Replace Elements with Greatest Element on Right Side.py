#1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for i in range(len(arr)-2,-1,-1):
            curVal = arr[i]
            arr[i] = mx
            if mx < curVal:
                mx = curVal
            
        return arr
                
            
