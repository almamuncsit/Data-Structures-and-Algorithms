class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next

    def AddAtBegining(self, new_data):
        NewNode = Node(new_data)
        NewNode.next = self.head
        self.head = NewNode

    def AddAtEnd(self, new_data):
        NewNode = Node(new_data)
        if self.head is None:
            self.head = NewNode
            return
        temp_val = self.head
        while temp_val.next:
            temp_val = temp_val.next
        temp_val.next = NewNode

    def AddInMiddle(self, middle_node, new_data):
        NewNode = Node(new_data)
        NewNode.next, middle_node.next = middle_node.next, NewNode

    def RemoveNode(self, remove_data):
        head_val = self.head

        # Remove if data is the first element
        if head_val is not None:
            if head_val.data == remove_data:
                self.head = head_val.next
                head_val = None
                return

        # find out the data node and previous node
        while head_val is not None:
            if head_val.data == remove_data:
                break
            prev = head_val
            head_val = head_val.next

        # Return if head val is empty
        if head_val == None:
            return

        # Remove item from linked list
        prev.next = head_val.next
        head_val = None


if __name__ == "__main__":
    list = SLinkedList()
    list.head = Node("Sat")

    e1 = Node("Sun")
    e2 = Node("Mon")

    list.head.next = e1
    e1.next = e2
    list.AddAtBegining('Welcome')
    list.AddAtEnd('Dhaka')
    list.AddInMiddle(e2, 'Mid')

    print("Before Remove")
    list.printList()

    print("After Remove")
    list.RemoveNode('Mon')
    list.printList()
