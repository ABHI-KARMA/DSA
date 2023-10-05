class Stack():
    def __init__(self):
        self.stack = []
        
    def action_create_stack(self):
        return self.stack
        
    def action_push_element(self, x):
        stk = self.action_create_stack()
        stk.append(x)
        
    def action_pop_element(self):
        if self.isEmpty():
            print("Stack Is Empty")
        else:
            self.stack.pop()
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
        
    def action_peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.stack[-1]
