# Function to find maximum of all adjacents
def maximumAdjacent(sizeOfArray, arr):
    start = 0
    end = 1
    
    # iterating with window of size two
    while(end < len(arr)):
        print(max(arr[start], arr[end]), end = ' ')
        start += 1
        end += 1
