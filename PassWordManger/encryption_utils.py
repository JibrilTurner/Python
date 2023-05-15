class EncryptionUtils:
    @staticmethod
    def encrypt(linked_list, key):
        curNode = linked_list.head.next
        while curNode is not None:
            curNode.password = curNode.password[::-1]
            curNode.username = curNode.username[::-1]
            curNode.identifier = curNode.identifier[::-1]
            curNode.encrpytionStandered = curNode.encrpytionStandered[::-1]
            curNode = curNode.next

    @staticmethod
    def decrypt(linked_list, key):
        curNode = linked_list.head.next
        while curNode is not None:
            curNode.password = curNode.password[::-1]
            curNode.username = curNode.username[::-1]
            curNode.identifier = curNode.identifier[::-1]
            curNode.encrpytionStandered = curNode.encrpytionStandered[::-1]
            curNode = curNode.next
