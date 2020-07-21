def countingSort(s,n):
    freq=[0 for i in range(256)] # store frequency of all characters present in the given string, initially 0.

    # increase the count of character frequency encountered.
    for char in s:
        freq[ord(char)]+=1

    # now iterate the frequency table and print the i th character , f[i] times.
    s = ""
    for i in range(256):
        for j in range(freq[i]):
            s += chr(i)
    return s
