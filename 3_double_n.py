# Gemini Advanced
# Sergei Chaparin

def double_each_n(n, current_value=None):
    """Doubles the current value at each iteration using recursion.

    Args:
        n: The number of iterations.
        current_value: The current value being doubled (initially None).

    Returns:
        The final doubled value after n iterations.
    """
    if n == 0:
        return current_value
    else:
        if current_value is None:
            current_value = 1  # Start with 1 if not provided
        return double_each_n(n - 1, current_value * 2)


# Example usage
result = double_each_n(20)
print(result)  # Output: 32 (1 -> 2 -> 4 -> 8 -> 16 -> 32)

# Yet another comment