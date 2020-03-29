class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next


if __name__ == "__main__":
    test_list = SLinkedList()
    test_list.head = Node("Saturday")

    e1 = Node("Sunday")
    e2 = Node("Monday")

    test_list.head.next = e1
    e1.next = e2

    test_list.print_list()
