
//User function Template for C++

// You need to insert the given element at the given index. 
// After inserting the elements at index, elements
// from index onward should be shifted one position ahead
// You may assume that the array already has sizeOfArray - 1
// elements.
void insertAtIndex(int arr[], int sizeOfArray, int idx, int element)
{
    //Your code here
    int i = 0;
    for (i = sizeOfArray-1; i>=idx;i--)
    {
        arr[i+1] = arr[i];
    }
    
    arr[idx] = element;
    
}
