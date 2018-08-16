'''
题目：
输入一个整形数组，数组里有正数也有负数。
数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。
求所有子数组的和的最大值。要求时间复杂度为O(n)。

例如输入的数组为1, -2, 3, 10, -4, 7, 2, -5，和最大的子数组为3, 10, -4, 7, 2，
因此输出为该子数组的和18。
'''
def max(i,j):
	if i>j:
		return i
	else:
		return j

def biggest_subarray(dp,lenth,intial_list):
	# lenth为母序列长度，intial_list为序列长度
	dp[0] = intial_list[0]# 边界条件
	#转移条件
	for i in range(lenth):
		dp[i] = max(intial_list[i],dp[i-1]+intial_list[i])
	#求最大子序列和
	sum = dp[0]
	for k in range(lenth):
		if(dp[k]>sum):
			sum = dp[k] 
	return sum
def main():
	intial_list = [1, -2, 3, 10, -4, 7, 2, -5]
	lenth = len(intial_list)
	dp=[0 for i in range(lenth)]
	sum = biggest_subarray(dp,lenth,intial_list)
	print(sum)


if __name__ == '__main__':
	main()