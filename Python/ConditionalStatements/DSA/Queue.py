class Queue:
	def __init__(self):
		self.queue=[]
	
	def isEmpty(self):
		return len(self.queue)==0
	
	def enque(self,element):
		self.queue.append(element)
		print("After Adding: ",self.queue)
	
	def deque(self):
		if not self.isEmpty():
			removed=self.queue.pop(0)
			print("Removed Element: ",removed)
	
	def peek(self):
		if not self.isEmpty():
			print("Top Element: ",self.queue[0])

a=Queue()
a.enque(78)
a.enque(98)
a.enque(45)
a.enque(32)
a.deque()
a.deque()
a.peek()
	