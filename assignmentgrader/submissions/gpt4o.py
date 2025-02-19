import time

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

def main():
    # Test cases
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(10) == 55
    
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(10) == 55
    
    print("All test cases passed.")
    
    # Measure execution time for the 50th Fibonacci number
    result_iter, time_iter = measure_time(fibonacci_iterative, 50)
    print(f"Iterative Fibonacci(50): {result_iter}, Time: {time_iter:.6f} seconds")
    
    # Measuring recursive approach for n=50 is not practical due to exponential complexity
    print("Measuring Fibonacci(50) for the recursive approach would take too long.")
    
if __name__ == "__main__":
    main()