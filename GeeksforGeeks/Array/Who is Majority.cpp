//User function Template for C++

/*Geeks, you have to complete this function*/

int majorityWins(int arr[], int n, int x,int y)
{
    int count_x=0;
    int count_y=0;
    
    // Iterating through the array elements
    // and incrementing the count accordingly
    for(int i=0;i<n;i++)
    {
        if(arr[i]==x)
        count_x++;
        if(arr[i]==y)
        count_y++;
    }
    
    // compare the elements and print accordingly
    if(count_x>count_y)
    return x;
    
    else if(count_y>count_x)
    return y;
    
    else
    return x<y?x:y;
    
}
