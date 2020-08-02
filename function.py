def standar(arg):
    print(arg)


def standar_with_pos(arg, /):
    print(arg)


standar(1)
standar_with_pos(10)

print('-----')


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')


fib(15)
