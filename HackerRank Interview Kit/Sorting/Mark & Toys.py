# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    count=0
    total=0

    for i in range(len(prices)):
        total+=prices[i]
        if total<=k:
            count+=1
    print(count) 
    return (count)
    
    
    
# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sortmylist(prices)
    count=0
    total=0

    for i in range(len(prices)):
        total+=prices[i]
        if total<=k:
            count+=1
    print(count) 
    return (count)

def sortmylist(nums):
    size = len(nums)
    for i in range(size-1):
        for j in range(size-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

