'''
题目：输入一个整数和一棵二元树。
从树的根结点开始往下访问一直到叶结点所经过的所有结点形成一条路径。
打印出和与输入整数相等的所有路径。
例如 输入整数22和如下二元树
    10  
  /   /   
 5    12   
/ \     
4  7
则打印出两条路径：10, 12和10, 5, 7。

二元树节点的数据结构定义为：
struct BinaryTreeNode // a node in the binary tree
{
int m_nValue; // value of node
BinaryTreeNode *m_pLeft; // left child of node
BinaryTreeNode *m_pRight; // right child of node
};
'''
l=[]
class BinarySearchTree:
	def __init__(self,Tree_list):
		if len(Tree_list)==0:
			return
		self.root=TreeNode(Tree_list[0])
		for i in range(1,len(Tree_list)):
			self._buildTree(self.root,Tree_list[i])
	def _buildTree(self,parent,val):
        # 建树，左右子树为空直接满足相应条件复制
        # 否则，递归左右子树建树
		
		if parent.val>val:
			if parent.left==None:
				parent.left=TreeNode(val)
				l.append(val)
			else:
				self._buildTree(parent.left,val)
		else:
			if parent.right==None:
				parent.right=TreeNode(val)
				l.append(val)
			else:
				self._buildTree(parent.right,val)
		print('l',l)
	def getRoot(self):
		return self.root
	def FindPath(self,root,expectNum):
		print('tree',l)
		res = []
		print(self.root.val)
		treepath = self.dfs(root)
		print(treepath)
		for i in treepath:
			print('sum',sum(map(int,i.split('->'))))
			if sum(map(int,i.split('->'))) ==expectNum:
				res.append(list(map(int,i.split('->'))))
		return res

	def dfs(self,root):
		if not root:
			return []
		if not root.left and not root.right:
			return [str(root.val)]
		treepath = [str(root.val)+'->'+path for path in self.dfs(root.left)]
		treepath += [str(root.val)+'->'+path for path in self.dfs(root.right)]
		print('dfs',treepath)
		return treepath
class TreeNode:
	def __init__(self,val,left=None,right = None):
		self.val = val
		self.left = left
		self.right = right
if __name__ == '__main__':
	Tree_list = [4,5,7,10,12]
	tree = BinarySearchTree(Tree_list)
	root = tree.getRoot()
	res = tree.FindPath(root,9)
	print(res)
