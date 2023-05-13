class parentNode: 
    def __init__(self, phoneNumber=None, firstName=None, lastName=None, email=None, address=None, city=None, state=None, zipCode=None, country=None):
        self.phoneNumber = phoneNumber
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.country = country
        self.next = None

class linkedList:
    def __init__(self):
        self.head = parentNode()

    def append(self, phoneNumber, firstName, lastName, email, address, city, state, zipCode, country):
        childNode = parentNode(phoneNumber, firstName, lastName, email, address, city, state, zipCode, country)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = childNode

    def appendExistingNone(self, index, value):
        curIdx = 0
        curNode = self.head
        while True:
            curNode = curNode.next
            if curIdx == index:
                if value is not None:
                    setattr(curNode, value[0], value[1])
                return
            curIdx += 1

    def display(self):
        sniffer = []
        cur_node = self.head.next
        while cur_node != None:
            sniffer.append((cur_node.phoneNumber, cur_node.firstName, cur_node.lastName, cur_node.email, cur_node.address, cur_node.city, cur_node.state, cur_node.zipCode, cur_node.country))
            cur_node = cur_node.next
        print(sniffer)

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

    def length(self):
        count = 0
        curNode = self.head.next
        while curNode:
            count += 1
            curNode = curNode.next
        return count
    
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



    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            curNode = self.head.next
            while cur_node is not None:
                file.write("Phone Number: {}\n".format(cur_node.phoneNumber))
                file.write("First Name: {}\n".format(cur_node.firstName))
                file.write("Last Name: {}\n".format(cur_node.lastName))
                file.write("Email: {}\n".format(cur_node.email))
                file.write("Address: {}\n".format(cur_node.address))
                file.write("City: {}\n".format(cur_node.city))
                file.write("State: {}\n".format(cur_node.state))
                file.write("Zip Code: {}\n".format(cur_node.zipCode))
                file.write("Country: {}\n".format(cur_node.country))
                file.write("\n")
                cur_node = cur_node.next

myList = linkedList()
myList.append("1234567890", "John", "Doe", None, None, None, None, None, None)

myList.display()
myList.write_to_file(myList.display(), "PhoneBook.txt")