'''
题目1：
有两个房间，一房间里有三盏灯，
另一房间里有控制着这三盏灯的三个开关，
这两个房间是分割开的，从一间里不能看到另一件的情况。
现在要求受训者分别进这两间房一次，
然后判断出这三盏灯分别是由哪个开关控制的。
思路：通过温度来解决
先在一个房间里，开十分钟a开关，再看2分钟b开关，回到
另一个房间触摸三盏灯的温度

题目2：

　　你让一些人为你工作了七天，你要用一根金条作为报酬。
金条被分成七小块，每天给出一块。如果你能将金条切割两次，
你怎样分给这些工人？
思路：1+2+4.

题目3：用一种算法来颠倒一个单链表。
'''
# -*- coding: utf-8 -*-
'''
链表逆序
'''
class ListNode:  
    def __init__(self,x):  
        self.val=x
        self.next=None 
 
'''
第一种方法：
对于一个长度为n的单链表head,用一个大小为n的数组arr储存从单链表从头
到尾遍历的所有元素，在从arr尾到头读取元素简历一个新的单链表
时间消耗O(n),空间消耗O(n)
'''       
def reverse_linkedlist1(head):
    if head == None or head.next == None: #边界条件
        return head
    arr = [] # 空间消耗为n,n为单链表的长度
    while head:
        arr.append(head.val)
        head = head.next
    newhead = ListNode(0)
    tmp = newhead
    for i in arr[::-1]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return newhead.next
 
'''
开始以单链表的第一个元素为循环变量cur,
并设置2个辅助变量tmp,保存数据;
newhead,新的翻转链表的表头。
时间消耗O(n),空间消耗O(1)
'''
 
def reverse_linkedlist2(head):
    if head == None or head.next == None: #边界条件
        return head
    cur = head #循环变量
    tmp = None #保存数据的临时变量
    newhead = None #新的翻转单链表的表头
    while cur:
        tmp = cur.next 
        cur.next = newhead
        newhead = cur   # 更新 新链表的表头
        print(newhead.val)
        cur = tmp
    return newhead
    
'''
开始以单链表的第二个元素为循环变量，用2个变量循环向后操作,并设置1个辅助变量tmp,保存数据;
时间消耗O(n),空间消耗O(1)
'''
 
 
def reverse_linkedlist3(head):
    if head == None or head.next == None: #边界条件
        return head
    p1 = head #循环变量1
    p2 = head.next #循环变量2
    tmp = None #保存数据的临时变量
    while p2:
        tmp = p2.next
        p2.next = p1
        p1 = p2
        p2 = tmp
    head.next = None
    return p1
 
'''
递归操作，先将从第一个点开始翻转转换从下一个节点开始翻转
直至只剩一个节点
时间消耗O(n),空间消耗O(1)
'''
 
def reverse_linkedlist4(head):
    if head is None or head.next is None:
        return head
    else:
        newhead=reverse_linkedlist4(head.next)
        head.next.next=head
        head.next=None
    return newhead
 
        
def create_ll(arr):
    pre = ListNode(0)
    tmp = pre
    for i in arr:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return pre.next
    
def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp=tmp.next
 
a = create_ll(range(5))
print_ll(a) # 0 1 2 3 4
# a = reverse_linkedlist1(a)
# print_ll(a) # 4 3 2 1 0
a = reverse_linkedlist2(a)
print_ll(a) # 0 1 2 3 4
# a = reverse_linkedlist3(a)
# print_ll(a) # 4 3 2 1 0
# a = reverse_linkedlist4(a)
# print_ll(a) # 0 1 2 3 4


'''
题目4：
不用乘法或加法增加8倍。现在用同样的方法增加7倍。
分析：n<<3  (n<<3)-n

题目5：
假设你有一个用1001个整数组成的数组，
这些整数是任意排列的，但是你知道所有的整数都在1到1000
（包括1000）之间。此外，除一个数字出现两次以外，
其他所有数字只出现一次。假设你只能对这个数组做一次处理，
用一种算法找出重复的那个数字。
如果你在运算中使用了辅助的存储方式，
那么你能找到不用这种方式的算法吗？
分析：
方法1：根据等差数列求和公式：n*(n+1)/2得，
sum-1000*(1000+1)/2 = result(其中sum是整个数组的和，
result是出现两次的那个数字).
方法2：根据题意，1~1000中只有一个数字出现了两次，
其他都出现了一次。则在原数组中再加入1~1000，
就成了只有一个数字出现了三次，其他数字都出现了两次，
可以用异或来解决.
'''