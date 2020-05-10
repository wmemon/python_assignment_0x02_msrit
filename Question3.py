from time import time


def performance(func):
    def wrap(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f" The time taken for the function to complete is :- {t2 - t1} seconds.")
    return wrap


@performance
def fib_iter(num):
    if not isinstance(num, int):
        return "[!]Enter a valid integer value of n."

    sum = 1
    start = 0
    for _ in range(num - 1):
        sum = sum + start
        prev_sum = sum - start
        start = prev_sum
    print(sum)
    return None


def fib_recur(num):
    if not isinstance(num, int):
        return "[!]Enter a valid integer value of n."
    if num == 2:
        return 1
    elif num == 1:
        return 1

    else:
        return fib_recur(num-1)+fib_recur(num-2)


t1 = time()
print(fib_recur(35))
t2 = time()
print(f"The time taken recursively is {t2-t1}. ")

fib_iter(35)
