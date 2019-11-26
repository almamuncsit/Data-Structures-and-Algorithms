class Stack():
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
    stack = Stack()
    stack.push('One')
    stack.push('Two')
    stack.push('Three')
    stack.push('Four')

    print('-- Before pop --')
    stack.print_stack()

    print('-- Start pop --')
    print(stack.pop())
    print('-- After pop -- ')
    stack.print_stack()

    print('-- After pop -- ')
    print(stack.pop())
    stack.print_stack()
