class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows >= 1:
            res.append([1])
            
        i = 1
        
        for i in range(1,numRows):
            
            nLen = len(res[i-1]) + 1
            
            curRow = [1 for i in range(nLen)]
            
            for j in range(1,nLen-1):
                curRow[j] = res[i-1][j] + res[i-1][j-1]
                
            
            res.append(curRow)
            
        return res
