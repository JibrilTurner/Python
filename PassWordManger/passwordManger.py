from typing import Any
import os

class parentNode: 
    def __init__(self, password = None, username = None, identifier = None, encrpytionStandered = None):
        self.password = password
        self.identifier = identifier
        self.username = username
        self.encrpytionStandered = encrpytionStandered
        self.next = None

class linkedList: # in this constructor, you will always wanna have the head node available
    def __init__(self): # the head node will never cotain data, and will always point to the first node
        self.head = parentNode() # as well as not being indexable


    def append(self,username, password ,identifier,encrpytionStandered):
        childNode = parentNode(username, password ,identifier,encrpytionStandered)
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
        cur_node = self.head.next
        while cur_node is not None:
            print(f"Username: {cur_node.username}\nPassword: {cur_node.password}\nIdentifier: {cur_node.identifier}\nEncryption Standard: {cur_node.encrpytionStandered}\n")
            cur_node = cur_node.next


    
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
        abs_path = os.path.abspath(filename)
        print("Writing to file:", abs_path)

        with open(abs_path, 'w') as file:
            curNode = self.head.next
            while curNode is not None:
                file.write(curNode.username)
                file.write(",")
                file.write(curNode.password)
                file.write(",")
                file.write(curNode.identifier)
                file.write(",")
                file.write(curNode.encrpytionStandered)
                file.write("\n")
                curNode = curNode.next
        print("File write complete.")

    def read_from_file(self, filename):
        abs_path = os.path.abspath(filename)
        print("Reading from file:", abs_path)

        with open(abs_path, 'r') as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                self.append(line[0], line[1], line[2], line[3])
        print("File read complete.")

    def encrypt(self, key): 
        curNode = self.head.next
        while curNode is not None:
            curNode.password = curNode.password[::-1]
            curNode.username = curNode.username[::-1]
            curNode.identifier = curNode.identifier[::-1]
            curNode.encrpytionStandered = curNode.encrpytionStandered[::-1]
            curNode = curNode.next

    def decrypt(self, key):
        curNode = self.head.next
        while curNode is not None:
            curNode.password = curNode.password[::-1]
            curNode.username = curNode.username[::-1]
            curNode.identifier = curNode.identifier[::-1]
            curNode.encrpytionStandered = curNode.encrpytionStandered[::-1]
            curNode = curNode.next

    def xorEncrypt(self, key, index):
        if len(key) != 1:
            raise ValueError("Key must be a single character.")
        
        curNode = self.head.next
        curIdx = 0
        while curNode is not None:
            if curIdx == index:
                curNode.password = "" if curNode.password is None else curNode.password
                curNode.username = "" if curNode.username is None else curNode.username

                curNode.password = self.xor(curNode.password, key)
                curNode.username = self.xor(curNode.username, key)
                break

            curNode = curNode.next
            curIdx += 1


    def xorDecrypt(self, key, index):
        if len(key) != 1:
            raise ValueError("Key must be a single character.")
        
        curNode = self.head.next
        curIdx = 0
        while curNode is not None:
            if curIdx == index:
                curNode.password = "" if curNode.password is None else curNode.password
                curNode.username = "" if curNode.username is None else curNode.username

                curNode.password = self.xor(curNode.password, key)
                curNode.username = self.xor(curNode.username, key)
                break

            curNode = curNode.next
            curIdx += 1


    @staticmethod
    def xor(data, key):
        if len(key) != 1:
            raise ValueError("Key must be a single character.")
        
        xored = ""
        for char in data:
            xored += chr(ord(char) ^ ord(key))
        return xored

def counter():
    count = 0
    while True:
        yield count
        count += 1
        return count





# Usage example:
myList = linkedList()
myList.append("JibrilTurner", " Use a single character as the key","Index 1" ,"XOR")

key = "s"  # Use a single character as the key
myList.display()  # Display the encrypted data

myList.xorDecrypt(key, 0)

myList.write_to_file("passwords.txt")

#python3 passwordManger.