'''
题目：输入一个整数数组，判断该数组是不是某二元查找树的后序遍历的结果。如果是返回true，否则返回false。
例如输入5、7、6、9、11、10、8，由于这一整数序列是如下树的后序遍历结果：
8 / \ 6 10 / \ / \ 5 7 9 11
因此返回true。
如果输入7、4、6、5，没有哪棵树的后序遍历的结果是这个序列，因此返回false。
思路：
分析：这是一道trilogy的笔试题，
主要考查对二元查找树的理解。
在后续遍历得到的序列中，最后一个元素为树的根结点。
从头开始扫描这个序列，
比根结点小的元素都应该位于序列的左半部分；
从第一个大于跟结点开始到跟结点前面的一个元素为止，
所有元素都应该大于跟结点，
因为这部分元素对应的是树的右子树。根据这样的划分，
把序列划分为左右两部分，
我们递归地确认序列的左、右两部分是不是都是二元查找树。
'''
class NodeTree:
	"""docstring for NodeTree"""
	def __init__(self, val,left=None,right=None):
		self.val = val
		self.right = right
		self.left = left
class solution:
	pass
	"""docstring for solution"""
def verifySquenceOfBST(squence,lenth):
	if squence == None or lenth<=0:
		return False
	root = squence[lenth-1]
	print('root',root)
	print('lenth',lenth)
	# 后序遍历中最后一个节点为根节点
	i = 0
	for k in range(lenth-1):
		if squence[k] >root:
			i = k
			break
	print('i',i)
	j = i
	for v in range(j,lenth-1):
		print('v-:',squence[v])
		if squence[v] <root:
			return False
	left =True
	if i>0:

		left = verifySquenceOfBST(squence,i)
		print('left',left)
	right = True
	if i<lenth-1:
		right = verifySquenceOfBST(squence[i:],lenth-i-1)
		print('right',right)
	return (right and left)
		
if __name__ == '__main__':
	squence = [5,7,6,9,11,10,8]
	# squence = [7,4,6,5]
	lenth = len(squence)
	# bst = solution()
	flag = verifySquenceOfBST(squence,lenth)
	print(flag)	
