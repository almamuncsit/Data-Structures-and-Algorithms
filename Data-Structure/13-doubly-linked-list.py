class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def add_to_middle(self, data, prev_data):
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == prev_data:
                new_node.next = current_node.next
                current_node.next = new_node
                new_node.previous = current_node
                new_node.next.previous = new_node

            current_node = current_node.next

    def pop(self):
        if self.tail is None:
            return 'List is empty'
        data = self.tail.data
        if self.tail.previous:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            self.tail = None
            self.head = None
        return data

    def print_first_to_last(self):
        current_node = self.head
        full_list = []
        while current_node:
            full_list.append(current_node.data)
            current_node = current_node.next
        print(full_list)

    def print_last_to_first(self):
        current_node = self.tail
        full_list = []
        while current_node:
            full_list.append(current_node.data)
            current_node = current_node.previous
        print(full_list)


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.prepend('Third')
    doubly_linked_list.prepend('Second')
    doubly_linked_list.prepend('First')
    doubly_linked_list.append('Fourth')
    doubly_linked_list.add_to_middle('Test', 'Two')
    doubly_linked_list.print_first_to_last()
    doubly_linked_list.print_last_to_first()

    print('-------Print head and tail --------')
    print(doubly_linked_list.head.data)
    print(doubly_linked_list.tail.data)

    print('-------Pop data--------')
    print(doubly_linked_list.pop())
    doubly_linked_list.print_first_to_last()
    print(doubly_linked_list.pop())
    print(doubly_linked_list.pop())
    print(doubly_linked_list.pop())
    print(doubly_linked_list.pop())
