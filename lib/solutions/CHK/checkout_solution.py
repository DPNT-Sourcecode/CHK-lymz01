# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    """
    skus = A string containing the SKUs of all the products in the basket
    """
    # Type checks
    if type(skus) != str:
        return -1

    # Create counters of A's and B's, after summing all variables we reduce
    # using special offers
    a_s = 0
    b_s = 0
    e_s = 0

    # Create a dictionary of prices
    prices_dict = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

    # Create a total price object:
    price_counter = 0

    # Iterate through the items
    for item in skus:
        # For non-implemented itemsType check:
        if item not in ["A", "B", "C", "D", "E"]:
            return -1
        elif item == "A":
            a_s += 1
        elif item == "B":
            b_s += 1
        elif item == "E":
            e_s += 1

        price_counter += prices_dict[item]

    # Create A discount:
    a_s_discount_by_5 = (a_s // 5) * (prices_dict["A"] * 5 - 200)
    remainder_after_5 = a_s % 5
    a_s_discount_by_3 = (remainder_after_5 // 3) * (prices_dict["A"] * 3 - 130)
    a_s_discount = a_s_discount_by_5 + a_s_discount_by_3

    # Apply E discount (Here I assume that we remove all B's that have been free)
    b_s_free = e_s // 2
    e_s_discount_to_b = min(b_s, b_s_free) * prices_dict["B"]

    # --- Substract those items that have been free
    b_s -= min(b_s, b_s_free)

    # Create B discount to the remaining non-free B's:
    b_s_discount = (b_s // 2) * (prices_dict["B"] * 2 - 45)

    price_counter = price_counter - (a_s_discount + e_s_discount_to_b + b_s_discount)

    return(price_counter)
