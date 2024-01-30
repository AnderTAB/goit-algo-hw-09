import timeit
from  typing import Callable

from dynamic import find_min_coins
from greedy import find_coins_greedy

def benchmark(func: Callable, num_: int):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(num)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'num': num_}, number=10)

if __name__ == '__main__':
    nums = [11, 123, 1123, 11123]
    results = []
    for num in nums:
        time = benchmark(find_min_coins, num)
        results.append((find_min_coins.__name__, num, time))   
        
        time = benchmark(find_coins_greedy, num)
        results.append((find_coins_greedy.__name__, num, time))
    
title = f"{'Метод':<30} | {'Кількість монет':<30} | {'Час виконання, сек'}"
print(title)
print("-" * len(title))
for result in results:
    print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")
         