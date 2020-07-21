
def merge_sort(nums):
    
	if len(nums) == 1:                                  
		return
		
	middle_index = len(nums) // 2
		
	left_half = nums[:middle_index]    #dividing 
	right_half = nums[middle_index:]
	
	merge_sort(left_half)              #recursive call 
	merge_sort(right_half)
	
	i = 0
	j = 0
	k = 0
	
	while i<len(left_half) and j<len(right_half):        #merging when both are there 
		if left_half[i] < right_half[j]:
			nums[k] = left_half[i]
			i = i + 1
		else:
			nums[k] = right_half[j]
			j = j + 1
			
		k = k + 1
		
	while i<len(left_half): 				#merging leftover left half
		nums[k] = left_half[i]
		k = k + 1
		i = i + 1	
		
	while j<len(right_half): 				#merging leftover right half
		nums[k] = left_half[j]
		k = k + 1
		j = j + 1	


	
if __name__ == "__main__":
   
   nums = [-3,-2,-1,1,2,1,0,-1,-2,-3]
   merge_sort(nums)
   print(nums)
  
