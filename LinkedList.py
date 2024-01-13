class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
      
class LinkedList():
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    def insert_head(self, data):
        new_node = Node(data) # creating node
        new_node.next = self.head # create connection
        self.head = new_node # reassign head
        self.n = self.n + 1 # increament length of LL
    
    def insert_tail(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1
    
    def __str__(self):
        result = ""
        curr = self.head
        while curr != None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]
    
    def insert_middle(self, data, item):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            if curr.next.data == item:
                break
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.n = self.n + 1
    
    def delete_head(self):
        if self.head == None:
            print("Empty Linked List")
        self.head = self.head.next
        self.n = self.n - 1
    
    def delete_tail(self):
        curr = self.head
        while curr.next != None:
            if curr.next.next == None:
                break
            curr = curr.next
        curr.next = None
        self.n = self.n - 1
    
    def delete_by_index(self, index):
        if index > self.n:
            print("IndexError : Index out of range")
        elif index == self.n and index != 1:
            self.delete_tail()
        elif index == 1:
            self.delete_head()
        else:
            pos = 0
            curr = self.head
            while curr.next != None:
                if index == pos:
                    break
                pos += 1
                curr = curr.next
            curr.next = curr.next.next
            self.n = self.n - 1
    
    def __getitem__(self, index):
        if index > self.n-1:
            return "IndexError: Index out of range"
        pos = 0
        curr = self.head
        while curr.next != None:
            if index == pos:
                break
            pos += 1
            curr = curr.next
        return curr.data
    
    def delete_by_value(self, data):
        curr = self.head
        if curr.next == None:
            self.delete_head()
            return 
        while curr.next != None:
            if curr.next.data == data:
                break
            curr = curr.next
        # breakpoint()
        if curr.next == None:
            print(f"{data} doesn't exist")
        else:
            curr.next = curr.next.next
            self.n = self.n - 1
    
    def insert_multiple(self, lst, index):
        item = self.__getitem__(index)
        for i in lst:
            self.insert_middle(i, item)
