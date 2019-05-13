def quickSort(nums):
	'''
	nums: list
	'''
	if len(nums)<2:
		return nums
	i=0
	j=len(nums)-1
	act=0# 0 for j 1 for i
	target=nums[0]
	while(i<j):
		if act==0:
			if nums[j]<target:
				nums[i]=nums[j]
				act=1
				i+=1
			else:
				j-=1
		else:
			if nums[i]>target:
				nums[j]=nums[i]
				act=0
				j-=1
			else:
				i+=1
	nums[i]=target
	n1=quickSort(nums[:i])
	n2=quickSort(nums[i+1:])
	res=n1
	res.append(target)
	res+=n2
	return res



if __name__=="__main__":
	nums=[5,4,3,2,1]
	print(nums)
	res=quickSort(nums)
	print(res)