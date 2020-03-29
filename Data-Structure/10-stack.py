class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return False

        return self.stack.pop()

    def print_stack(self):
        for item in self.stack:
            print(item)


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push('First')
    my_stack.push('Second')
    my_stack.push('Third')
    my_stack.push('Fourth')

    print('-- Before pop --')
    my_stack.print_stack()

    print('-- Start pop --')
    print(my_stack.pop())
    print('-- After pop -- ')
    my_stack.print_stack()

    print('-- After pop -- ')
    print(my_stack.pop())
    my_stack.print_stack()
