def nextArray(p):
	nxt=[0]*len(p)
	for i in range(1,len(p)):
		for j in range(1,i+1):
			if p[:j]==p[i+1-j:i+1]:
				nxt[i]=j
	return nxt
def kmp(s,p,nxt):
	found=False
	for i in range(len(s)):
		j=0
		while(j<len(p) and i<len(s)):
			print('i=',i,s[i],'j=',j,p[j])
			if s[i]==p[j]:
				i+=1
				j+=1
			else:
				if j==0:
					i+=1
				else:
					j=nxt[j]
		if j==len(p):
			found=True
			break
	if found:
		return i-j
	else:
		return -1


if __name__ == "__main__":
	s="ABCDABCDABDE"
	p="ABCDABD"
	nxt=nextArray(p)
	print(nxt)
	res=kmp(s,p,nxt)
	print(res)


