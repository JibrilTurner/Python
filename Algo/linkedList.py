from typing import Any

class parentNode: 
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedList: # in this constructor, you will always wanna have the head node available
    def __init__(self): # the head node will never cotain data, and will always point to the first node
        self.head = parentNode() # as well as not being indexable




    # functions to manipulate the linked list

    def append(self, data): # so this funtion will be able to add elements to the linked list, make sure to pass in data
        childNode = parentNode(data)# creating a new node and passing in data
        cur = self.head # creating a node to know where we are in the linked list
        while cur.next != None: # so while the next element is not none, we will keep moving forward.
            cur = cur.next # so we will keep moving forward
        cur.next = childNode # once we reach the end of the linked list, we will add the new node to the end of the linked list

    def length(self): # this is only passing the instance of the class
        cur = self.head # creating a node to know where we are in the linked list
        total = 0 # creating a variable to keep track of the total number of nodes
        while cur.next != None:
            total += 1 
            cur = cur.next # so we will keep moving forward
        return total 
    
    def display(self): # to display the contents of the linked list
        sniffer = [] # creating a list to store the elements weve traversed
        cur_node = self.head # creating a node to know where we are in the linked list
        while cur_node.next != None: # so while the next element is not none, we will keep moving forward.
            cur_node = cur_node.next # so we will keep moving forward
            sniffer.append(cur_node.data) # gathering the data from the node and appending it to the list
        print(sniffer) # so we will print the list

    def get(self,index):
        if index >= self.length(): # so if the index is greater than the length of the linked list  
            print("ERROR: 'Get' Index out of range!") # will print an error message
            return None # and return
        curIdx = 0 # creating a variable to keep track of the index
        curNode = self.head # creating a node to know where we are in the linked list
        while True: # so while true
            curNode = curNode.next # so we will keep moving forward
            if curIdx == index: 
                return curNode.data # so if the current index is equal to the index we are looking for, we will return the data
            curIdx += 1 # so we will keep moving forward
    
    def erase(self, index):
        if index >= self.length(): # so if the index is greater than the length of the linked list
            print("ERROR: 'Erase' Index out of range!") # will print an error message
            return
        curIdx = 0 # creating a variable to keep track of the index
        curNode = self.head # creating a node to know where we are in the linked list
        while True: # so while true
            lastNode = curNode # so we will keep moving forward
            curNode = curNode.next # so we will keep moving forward
            if curIdx == index: # so if the current index is equal to the index we are looking for
                lastNode.next = curNode.next # we will set the last node to point to the node after the current node, Erasing current node 
                return
            curIdx += 1 # so we will keep moving forward



myList = linkedList() # creating an instance of the linked list

myList.append(1) # adding elements to the linked list
myList.append(2)
myList.append(3)
myList.append(4)
myList.erase(2)
myList.display() # displaying the contents of the linked list

print("Element at 2nd index: %d" % myList.get(2)) # getting the element at the 2nd index