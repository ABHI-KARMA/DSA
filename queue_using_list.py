class Queue():
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        if len(self.queue) <= 0:
            return True
        return False
    def enqueue(self, x):
        self.queue.append(x)
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.queue.pop(0)
    def get_queue(self):
        return self.queue
