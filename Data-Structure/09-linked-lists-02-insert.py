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

    def add_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp_val = self.head
        while temp_val.next:
            temp_val = temp_val.next
        temp_val.next = new_node

    def add_in_middle(self, middle_node, new_data):
        new_node = Node(new_data)
        new_node.next, middle_node.next = middle_node.next, new_node


if __name__ == "__main__":
    linked_list = SLinkedList()
    linked_list.head = Node("Sat")

    e1 = Node("Sun")
    e2 = Node("Mon")

    linked_list.head.next = e1
    e1.next = e2
    linked_list.add_at_beginning('Welcome')
    linked_list.add_at_end('Dhaka')
    linked_list.add_in_middle(e2, 'Mid')

    linked_list.print_list()
