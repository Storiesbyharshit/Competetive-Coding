
def insertion_sort(nums):
    
	for i in range(len(nums)):
		
		j = i                          			#sort elements from i to 0
		
		while j>0 and nums[j-1] > nums[j]:  c		#swap if left is greater than right
			swap(nums,j,j-1)
			j = j - 1				#iterating towards left
	
	return nums
	
def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
 
if __name__ == "__main__":
   
   nums = [5,4,3,2,1]
   print(insertion_sort(nums))
  
