# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    """
    x: A positive integer between 0-100
    y: A positive integer between 0-100

    Returns an integer representing the sum of both numbers
    """
    # Checks of type and value
    if (type(x) != int) or (type(y)!= int):
        raise TypeError("Both numbers should be integers")

    if (x < 0) or (x > 100) or (y < 0) or (y > 100):
        raise ValueError("Input integers should lie between 0 and 100")

    return(x + y)

