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


if __name__ == "__main__":
    list = SLinkedList()
    list.head = Node("Sat")

    e1 = Node("Sun")
    e2 = Node("Mon")

    list.head.next = e1
    e1.next = e2

    list.printList()
