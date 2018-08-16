'''
第7题（链表）
微软亚院之编程判断俩个链表是否相交
给出俩个单向链表的头指针，比如h1，h2，判断这俩个链表是否相交。
为了简化问题，我们假设俩个链表均不带环。

问题扩展：
1.如果链表可能有环列?
2.如果需要求出俩个链表相交的第一个节点列?
思路：
如果两个单链表有共同的节点，那么从第一个共同节点开始，
后面的节点都会重叠，直到链表结束。 
因为两个链表中有一个共同节点，
则这个节点里的指针域指向的下一个节点地址一样，
所以下一个节点也会相交，
依次类推。所以，若相交，则两个链表呈“Y”字形
思路：双指针解法 ，时间复杂度O(n+m)，空间复杂度O(1):

维护两个指针pA和pB，初始分别指向A和B。然后让它们分别遍历整个链表，每步一个节点。

当pA到达链表末尾时，让它指向B的头节点；类似的当pB到达链表末尾时，重新指向A的头节点。

如果pA在某一点与pB相遇，则pA或pB就是交点。

所以最多遍历 链表A的长度+链表B的长度 即可判断出是否有相交的节点。

'''
class ListNode:
	"""docstring for NodeList"""
	def __init__(self, val,next = None):
		self.val = val
		self.next = next
class solution:
	def raw_search(self,headA,headB):
	# 方法一：暴力遍历,判断相交，且无环的情况下
		pA = headA
		pB = headB
		if headA ==None or headB ==None:
			return
		c1 = pA
		while pA:
			c1 = pA
			pA = pA.next
		c2 = pB
		while pB:
			c2 = pB
			pB = pB.next
		if c1 == c2:
			return True
	def double_p(self,headA,headB):
		# 双指针法，可判断无环，并且找出相交点
		pA = headA
		pB = headB
		if headA ==None or headB ==None:
			# 其中有一个为空链表，就不存在相交的可能
			return
		while pA and pB:
			if pA.val != pB.val:
				if pA.next and pB.next:
					pA = pA.next
					pB = pB.next
				elif pA.next==None and pB.next!=None:
					pA = headB
					pB = pB.next
				elif pB.next == None and pA.next!=None:
					pB =headA
					pA = pA.next
				else:
					return
			else:
				return pA
	def hasCycle(head):
		# 判断是否有环
		fast = head
		slow = head
		while (fast and fast.next):
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				return slow
		return None
	def slow_fast_p(self,headA,headB):
		# 快慢指针法，针对有环，并且能输出相交节点
		pos1 = self.hasCycle(headA)
		pos2 = self.hasCycle(headB)
		# 两个链表都有环
		if pos1 and pos2:
			tmp = pos1
			# 判断这两个环是不是同一个环
			while pos1!=tmp:
				if pos1 == pos2 ||pos1.next == pos2:
					break
				pos1 = pos1.next.next
				tmp = tmp.next
			# 两个链表的环不是同一个环，所以没有交点
			if pos1!=pos2 and pos1.next != pos2:
				return None
			#两个链表有共同的交点pos1，现在求第一个交点
			len1 = 0
			len2 = 0
			nd1 = headA
			while nd1 != pos1 :
				len1 +=1
				nd1 = nd1.next
			nd2 = headB
			while nd2 != pos1:
				len2 +=1
				nd2 = nd2.next
			# 较长链表的链表的nd先走了dif步
			dif = 0
			nd1,nd2 = headA,headB
			if len1>=len2:
				dif = len1-len2
				while dif:
					dif -=1
					nd1 = nd1.next
			else:
				dif = len2-len1
				while dif:
					dif -=1
					nd2 = nd2.next
			# 之后两个nd再一起走，直到nd相等（即为第一个交点）
			while nd1 != pos1 and nd2 !=pos1:
				if nd1 == nd2:
					return nd1
				nd1 =nd1.next
				nd2 =nd2.next
			return pos1