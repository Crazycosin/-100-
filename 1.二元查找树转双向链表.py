'''
Created on 2017-1-9
1.把二元查找树转变成排序的双向链表（树） 
 题目： 
输入一棵二元查找树，将该二元查找树转换成一个排序的双向链表。 
要求不能创建任何新的结点，只调整指针的指向。 
   10 
  / / 
  6  14 
 / / / / 
4  8 12 16 
 转换成双向链表 
4=6=8=10=12=14=16。 
  
 首先我们定义的二元查找树 节点的数据结构如下： 
 struct BSTreeNode 
{ 
  int m_nValue; // value of node 
  BSTreeNode *m_pLeft; // left child of node 
  BSTreeNode *m_pRight; // right child of node 
}; 
@author: admin
'''
"""
二元查找树： 它首先要是一棵二元树，在这基础上它或者是一棵空树；或者是具有下列性质的二元树： 
（1）若左子树不空，则左子树上所有结点的值均小于它的父结点的值；
 （2）若右子树不空，则右子树上所有结点的值均大于等于它的根结点的值；
  （3）左、右子树也分别为二元查找树
  思路：二叉查找树按中序遍历得到的数据是按顺序排列的，
  所以要按照中序遍历的顺序把二叉树转换成链表；
  二叉树每一个结点有两个指针left，right，
  和链表的前驱和后继对应的指针正好对应。
"""
class BinarySearchTree:
    def __init__(self,source):
        if len(source)==0:
            return
        self.root=TreeNode(source[0])
        for i in range(1,len(source)):
            self._buildTree(self.root,source[i])
    def _buildTree(self,parent,data):
        # 建树，左右子树为空直接满足相应条件复制
        # 否则，递归左右子树建树
        if parent.data>data:
            if parent.left==None:
                parent.left=TreeNode(data)
            else:
                self._buildTree(parent.left,data)
        else:
            if parent.right==None:
                parent.right=TreeNode(data)
            else:
                self._buildTree(parent.right, data)
    def transform(self):
        # 转换入口，先判断树是否为空
        if self.root==None:
            return
        self.nodeList=[]
        self.transformRec(self.root)
        self._reAssemble()       
    def transformRec(self,parent):
        if(parent.left!=None):
            print(parent.left.data)
            self.transformRec(parent.left)
        # 将二叉排序树的元素节点用列表存起来
        self.nodeList.append(parent)
        for i in range(0,len(self.nodeList)):
            print(self.nodeList[i].data,"%s"%i)
        if(parent.right!=None):
            self.transformRec(parent.right)
    def _reAssemble(self):
        # 建立双向链表的过程：
        # 1.初始话第一个节点的左子树，也是双向链表中的第一个元素的前驱
        # 2.在未遍历到最后一个节点之前，交换复制左右子树跟前驱后继
        # 3.最后一个元素只有前驱没有后继，所以置空后继
        for i in range(0,len(self.nodeList)):
            if i==0:
                if len(self.nodeList)>1:
                    self.nodeList[i].left=None
                    self.nodeList[i].right=self.nodeList[i+1]
                else:
                    self.nodeList[i].left=None
                    self.nodeList[i].right=None
            elif i==len(self.nodeList)-1:
                if len(self.nodeList)>1:
                    self.nodeList[i].right=None
                    self.nodeList[i].left=self.nodeList[i-1]
            else:
                self.nodeList[i].left=self.nodeList[i-1]
                self.nodeList[i].right=self.nodeList[i+1]
    def printData(self):
        node=self.nodeList[0]
        while(node!=None):
            print(node.data,end=",")
            node=node.right
class TreeNode:
    # 建立树节点，初始左右节点为空
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right 
 
if __name__ == '__main__':
    source=[6,3,1,8,2,7,5,4]
    tree=BinarySearchTree(source)
    tree.transform()
    tree.printData()
