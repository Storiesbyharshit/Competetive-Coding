Python 3

def minimumJumps(arr, n):
    if n <= 1:            # If n is less than 1 no jumps are required
        return 0
    if arr[0] == 0:       # If first element is 0, we can't jump to any point return -1
        return -1

    maxrange = arr[0]     # Define maxRange for first element (Greedy Approach
    steps = arr[0]        # Steps allowed from first element
    jumps = 1             # Number of jumps required

    for i in range(1, n):
        if i == n - 1:              # If we reached the end return the number of jumps
            return jumps
            
        # calculate maxrange by comparing the current max range from current value
        maxrange = max(maxrange, i + arr[i]) 
        steps -= 1  # we use a step to get to the current index 

        if steps == 0:              # If steps is 0
            jumps += 1              # Increase the number of jumps
            if i >= maxrange:       # If maxRange is less than equal to i we can't move further, return -1
                return -1
            steps = maxrange - i    # New Steps value is calculated as maxRange-i.
    return -1

