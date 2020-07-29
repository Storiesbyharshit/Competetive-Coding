import bisect

n, d = map(int, input().split())
E = list(map(int, input().split()))

count = 0
B = sorted(E[:d]) #median windown

for i in range(d, n):
    median = (B[(d-1)//2] + B[d//2])/2 #calculating median
    if E[i] >= 2*median:
        count += 1
    del B[bisect.bisect_left(B, E[i-d])] #deleting traiing element
    bisect.insort_left(B, E[i])#sorting for median

    """
    by using the bisect module, and keeping a tab of the numbers to insert and delete from the fixed length sliding window:

The element to remove is always present in the window, so the bisect module can help to find its postion in sorted array (the elements of the window is needed to be sorted to find median).

The bisect can then be used to insert the inserting number into the sorted window, keeping it sorted on insert.
    """
print(count)
