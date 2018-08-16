'''
Created on 2017-1-9
2.设计包含min函数的栈（栈）
定义栈的数据结构，要求添加一个min函数，能够得到栈的最小元素。
要求函数min、push以及pop的时间复杂度都是O(1)。
@author: admin
思路：设置俩个列表，aux列表放置倒序的值，main列表为正常的栈存储
'''
class MinStack:
    def __init__(self):
        self.mainAry=[]
        self.auxAry=[]
    def push(self,data):
        if len(self.mainAry)==0:
            self.auxAry.append(data)
        elif data<=self.auxAry[len(self.auxAry)-1]:
            self.auxAry.append(data)
        self.mainAry.append(data)
    def pop(self):
        if len(self.mainAry)==0:
            raise IndexError
        data=self.mainAry[len(self.mainAry)-1]
        del self.mainAry[len(self.mainAry)-1]
        if data==self.auxAry[len(self.auxAry)-1]:
            del self.auxAry[len(self.auxAry)-1]
        return data
    def min(self):
        if len(self.auxAry)==0:
            raise IndexError
        else:
            return self.auxAry[len(self.auxAry)-1]        
if __name__ == '__main__':
    stack=MinStack()
    stack.push(7)
    stack.push(5)
    stack.push(9)
    stack.push(2)
    stack.push(4)
    print(stack.pop())
    print(stack.min())
    print(stack.pop())
    print(stack.min())
    print(stack.pop())
    print(stack.min())
    print(stack.pop())
    print(stack.min())
