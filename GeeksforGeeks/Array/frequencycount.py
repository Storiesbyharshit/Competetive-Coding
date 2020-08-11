def frequencycount(A,N):
    # code here
    import collections
    freq_dict = collections.Counter(A)
    return freq_dict.values()
    
