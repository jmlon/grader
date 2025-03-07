import time

class FibonacciCalculator:
    """
    A class to compute Fibonacci numbers using different methods and measure their execution times.
    """

    def __init__(self):
        pass

    def fibonacci_iterative(self, n):
        """
        Computes the n-th Fibonacci number iteratively.

        Args:
            n: The index of the desired Fibonacci number (non-negative integer).

        Returns:
            The n-th Fibonacci number.  Returns 0 if n < 0.
        Raises:
            TypeError: if input n is not an integer
        """
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")

        if n < 0:
            return 0  # Handle negative input (return 0 as a convention)
        elif n <= 1:
            return n  # Base cases: F(0) = 0, F(1) = 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    def fibonacci_recursive(self, n):
        """
        Computes the n-th Fibonacci number recursively.

        Args:
            n: The index of the desired Fibonacci number (non-negative integer).

        Returns:
            The n-th Fibonacci number. Returns 0 if n < 0.
        Raises:
            TypeError: if input n is not an integer
        """
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")
        if n < 0:
            return 0 # Handle negative input.
        elif n <= 1:
            return n  # Base cases: F(0) = 0, F(1) = 1
        else:
            return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def measure_execution_time(self, func, *args):
        """
        Measures the execution time of a given function.

        Args:
            func: The function to be timed.
            *args: The arguments to be passed to the function.

        Returns:
            A tuple containing:
            - The result of the function call.
            - The execution time in seconds (float).
        """
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time



def main():
    """
    Main function to test and time the Fibonacci functions.
    """
    calculator = FibonacciCalculator()

    # Test cases with assertions
    test_cases = [
        (-1, 0),
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55),
        (20, 6765)
    ]
    for n, expected in test_cases:
        assert calculator.fibonacci_iterative(n) == expected, f"Iterative F({n}) failed"
        assert calculator.fibonacci_recursive(n) == expected, f"Recursive F({n}) failed"
    print("All test cases passed!")

    # Measure execution time for the 35-th Fibonacci number (to see difference)
    n = 35
    iterative_result, iterative_time = calculator.measure_execution_time(calculator.fibonacci_iterative, n)
    recursive_result, recursive_time = calculator.measure_execution_time(calculator.fibonacci_recursive, n)

    print(f"Fibonacci({n}) - Iterative: Result = {iterative_result}, Time = {iterative_time:.6f} seconds")
    print(f"Fibonacci({n}) - Recursive: Result = {recursive_result}, Time = {recursive_time:.6f} seconds")

     # Measure execution time for the 50-th Fibonacci number.  Iterative only.
    n_large = 50
    iterative_result_large, iterative_time_large = calculator.measure_execution_time(calculator.fibonacci_iterative, n_large)
    #  The recursive version will take far too long.  Avoid running it.
    # recursive_result_large, recursive_time_large = calculator.measure_execution_time(calculator.fibonacci_recursive, n_large)


    print(f"Fibonacci({n_large}) - Iterative: Result = {iterative_result_large}, Time = {iterative_time_large:.6f} seconds")
    #print(f"Fibonacci({n_large}) - Recursive: Result = {recursive_result_large}, Time = {recursive_time_large:.6f} seconds")  # Commented out

    # Test invalid input
    try:
        calculator.fibonacci_iterative(3.14)
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    try:
        calculator.fibonacci_recursive("abc")
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")



if __name__ == "__main__":
    main()