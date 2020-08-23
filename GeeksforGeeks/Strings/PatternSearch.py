def search(p,s):
    #code here
    # if p in s:
    #     return True
    # return False
    w_l = len(p)
    txt_l = len(s)
    for i in range(txt_l):
        if i+w_l <= txt_l:
            if s[i:i+w_l] == p:
                return True
    return False
