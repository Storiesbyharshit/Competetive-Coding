class Solution:
	def divisorGame(self, N: int) -> bool:
		result=[False for i in range(N+1)]
		for i in range(2,N+1):
			for j in range(1,i):
				if i%j==0 and result[i-j]==False:
					result[i]=True
					break
		return result[N]
    
class Solution(object):
    def divisorGame(self, N):
        return N%2==0
