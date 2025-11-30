# utils.py
# Helper functions for Food Delivery Analysis project

def average(values):
    """Calculate the average of a list of numbers."""
    if len(values) == 0:
        return 0
    return sum(values) / len(values)

def max_value(values):
    """Return the maximum value from a list."""
    if len(values) == 0:
        return None
    return max(values)

def min_value(values):
    """Return the minimum value from a list."""
    if len(values) == 0:
        return None
    return min(values)

def count_items(values):
    """Return the number of items in a list."""
    return len(values)
