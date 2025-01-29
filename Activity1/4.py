def stats_decorator(func):
    """Decorator to compute and print statistics of numbers."""
    def wrapper(t):
        """Wrapper to compute and display statistics for numbers."""
        numbers = func(t)
        print(f"Numbers read: {numbers}")
        print(f"Count of numbers: {len(numbers)}")
        print(f"Average of numbers: {sum(numbers) / len(numbers):.2f}")
        print(f"Maximum of numbers: {max(numbers)}")
        return numbers
    return wrapper

@stats_decorator
def printState(t):
    """Reads integers from a file and returns them as a list."""
    with open(t, "r") as file:
        data = [int(line.strip()) for line in file if line.strip().isdigit()]
    return data
