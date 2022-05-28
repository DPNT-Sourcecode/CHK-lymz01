# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    """
    skus = A string containing the SKUs of all the products in the basket
    """
    # Type checks
    if type(skus) != str:
        raise TypeError("Skus should be a string.")

    # Turn the string into uppercase letters:
    skus = skus.upper()

    # Create counters of A's and B's, after summing all variables we reduce
    # using special offers
    a_s = 0
    b_s = 0

    # Create a dictionary of prices
    prices_dict = {"A": 50, "B": 30, "C": 20, "D": 15}

    # Create a total price object:
    price_counter = 0

    # Iterate through the items
    for item in skus:
        # Type check:
        if item not in ["A", "B", "C", "D"]:
            raise ValueEror("Only items A, B, C, and D are allowed.")
        elif item == "A":
            a_s += 1
        elif item == "B":
            b_s += 1

        price_counter += prices_dict[item]

    # Create A discount:
    a_s_discount = (a_s // 3) * (50 * 3 - 130)

    # Create B discount:
    b_s_discount = (b_s // 2) * (30 * 2 - 45)

    price_counter = price_counter - a_s_discount - b_s_discount

    return(price_counter)



