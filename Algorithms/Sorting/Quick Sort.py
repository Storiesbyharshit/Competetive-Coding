
def quick_sort(nums,low,high):
    
	if low >= high:
		return
		
	pivot_index = partition(nums,low,high)
	
	quick_sort(nums,low, pivot_index-1) #recursive call
	quick_sort(nums, pivot_index+1,high)
	
	
def partition(nums,low,high):

	pivot_index = (low+high)//2
	
	swap(nums,pivot_index,high) #swap pivot and high
	
	i = low 				#i=low 
	
	for j in range(low,high):
		if nums[j] <= nums[high]:
			swap(nums,i,j)   #swap with low if j is less than high 
			i = i + 1		#increasing low
			
	swap(nums,i,high) #swap i and high 
	
	return i
	
def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
	
	
if __name__ == "__main__":
   
   nums = [-2,-1,0,1,0,-1,-2]
   quick_sort(nums,0,len(nums)-1)
   print(nums)
  
