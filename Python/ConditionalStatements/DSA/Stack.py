class Stack:
	def __init__(self):
		self.stack=[]
		
	def isEmpty(self):
		return len(self.stack)==0
	
	def push(self,data):
		self.stack.append(data)
		print("After Adding: ",self.stack)
	
	def pop(self):
		if not self.isEmpty():
			removed=self.stack.pop()
			print("Element Removed: ",removed)
	
	def peek(self):
		if not self.isEmpty():
			print("Top Element is: ",self.stack[-1])
			
a=Stack()
a.push(67)
a.push(32)
a.push(99)
a.pop()
a.peek()
a.push(73)
		