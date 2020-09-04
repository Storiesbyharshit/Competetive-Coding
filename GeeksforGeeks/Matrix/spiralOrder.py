class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_beg, row_end, col_beg, col_end = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        while row_beg <= row_end and col_beg <= col_end:
            #left -> right
            for i in range(col_beg, col_end+1):
                res.append(matrix[row_beg][i])
            row_beg += 1
            
            #right -> bottom
            for i in range(row_beg, row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            
            #right -> left
            if row_beg <= row_end:
                for i in range(col_end, col_beg-1, -1):
                    res.append(matrix[row_end][i])
            row_end -= 1
            
            #bottom -> top
            if col_beg <= col_end:
                for i in range(row_end, row_beg-1, -1):
                    res.append(matrix[i][col_beg])     
            col_beg += 1
            
        return res
        
