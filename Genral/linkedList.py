class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None 


class linkedList:
    def __init__(self): 
        self.head = node()
        
    def append(self,data): #passing in the data 
        newNode = node(data) # sets the data point inside the node 
        current = self.head # once the next node of the current node equals none that means it at the end of the list. Locating where you should append 
        while current.next!=None:
            current = current.next
        current.next = newNode
    
    def length(self): # only passing the instnace of the class
        current = self.head
        total = 0; 
        while current.next != None: 
            total += 1 
            current = current.next
        return total
    
    def display(self): # 
        