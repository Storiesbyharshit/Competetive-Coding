def solve(m,n):
    '''
    :param m: number of rows
    :param n: number of columns
    :return: total possibilities
    '''
    # specifying the directions to check in i.e 8 directions
    x_off = [-2,-2,-1, 1, 2, 2, 1, -1]
    y_off = [-1, 1, 2, 2, 1,-1, -2, -2]
    MOD = 1000000007

    # variable to maintain number of positions which are not feasible
    ret = 0

    # iterating for complete matrix
    for i in range(m):
        for j in range(n):
            for k in range(8):
                x = i + x_off[k]
                y = j + y_off[k]
                # checking if the attack position is within bounds
                if x>=0 and x<m and y>=0 and y<n :
                    ret+=1 # if in bounds it is not feasible, increment it

    total = ((m*n)*(m*n-1))%MOD # total possible combinations of 2 knights
    return (total +MOD - ret)%MOD # returning total feasible combinations
