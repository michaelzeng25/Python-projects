
from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None # head points to nothing-am empty list

    def Add(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head # points to none after adding the first element
        self.head = new_node

    def PrintList(self):
        temp = self.head # cant use self.head to print the list or it will destroy the list.
        list = []
        while (temp != None):
            list.append(temp.data)
            temp = temp.next
        print(list)

    def getCount(self):
        temp = self.head
        count = 0

        while (temp):
            count += 1
            temp = temp.next
        return count

    def Reverse(self):
        prev = None
        temp = self.head
        while (temp is not None):
            next = temp.next
            temp.next = prev
            prev = temp # moving the prev from left to right each time and set it as the head
            temp = next
        self.head = prev # prev.data is the very first element from the right

    def deleteNode(self, position):

        if self.head == None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

if __name__ == '__main__':
    Llist = LinkedList()
    for _ in range(10):
        Llist.Add(randint(0,100))

    print ('The linked list contains:')
    Llist.PrintList()

    print("\nCount of nodes is :", Llist.getCount())

    Llist.Reverse()
    print('Reversed list:')
    Llist.PrintList()

    Llist.deleteNode(4) # 3 should be deleted
    Llist.PrintList()













