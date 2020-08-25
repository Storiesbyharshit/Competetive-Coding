def modified(s):
	ans=0
	same=1

	for i in range(1,len(s)):
		if(s[i]==s[i-1]):
			same+=1
		else:
			ans+=(same-1)//2
			same=1
	ans+=(same-1)//2

	return ans
