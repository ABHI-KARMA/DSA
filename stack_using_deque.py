from collection import deque

class StackDeque():
	def __init__(self):
		self.stack = deque()

	def action_get_stack(self):
		return self.stack

	def action_push(self, x):
		self.stack.append(x)

	def action_pop(self):
		if len(self.stack) == 0:
			print("Stack is Empty")
		else:
			self.stack.pop()
	