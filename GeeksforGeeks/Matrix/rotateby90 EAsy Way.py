class Solution:
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

 
def rotateby90(a, n): 
    #Your code here
    
    for r in zip(*a):
        a.append(list(r))
        
    i=0
    j=len(a)-1
    while i<j:
        a[i], a[j] = a[j], a[i]
        i+=1
        j-=1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(0,len(matrix)//2):
            temp = matrix[i]
            matrix[i] = matrix[len(matrix)-1-i]
            matrix[len(matrix)-1-i] = temp
        
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
