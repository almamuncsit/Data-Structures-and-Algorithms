import pytest


class Fibonacci():
    def __init__(self):
        self.i = 1

    def finbonacci(self, n):
        self.i += 1
        if self.fib_data[n]:
            return self.fib_data[n]
        if n in [1, 2]:
            return 1
        self.fib_data[n] = self.finbonacci(n-1) + self.finbonacci(n-2)
        return self.fib_data[n]


    def unit_test(self):
        assert self.finbonacci(1) == 1
        assert self.finbonacci(2) == 1
        assert self.finbonacci(3) == 2
        assert self.finbonacci(4) == 3
        assert self.finbonacci(5) == 5
        assert self.finbonacci(6) == 8
        assert self.finbonacci(7) == 13
        assert self.finbonacci(8) == 21


    def main(self):
        n = int(input())
        self.fib_data = [False]*(n+1)
        self.unit_test()
        print( 'Fibonacci: ', self.finbonacci(n) )


if __name__ == '__main__':
    fibonacci = Fibonacci()
    fibonacci.main()
    print("Total Iteration: ", fibonacci.i)

