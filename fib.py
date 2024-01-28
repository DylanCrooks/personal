from functools import lru_cache
import time
import matplotlib.pyplot as plt

dictstore = {}
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        arg = args[0]
        print(f" Executed in {elapsed_time:.9f} seconds: {func.__name__}({arg}) -> {result}")
        dictstore.update({arg:elapsed_time})
        return result
    return wrapper


@lru_cache
@timer
def fib(n:int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def plotting(x1: int = 1, x2: int = 100):
    fib(x2)
    n_vals = (dictstore.keys())
    execution_times = (dictstore.values())
    plt.plot(n_vals, execution_times, marker='o')
    plt.title('Execution Time vs n for Fibonacci Function')
    plt.xlabel('n')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plotting()