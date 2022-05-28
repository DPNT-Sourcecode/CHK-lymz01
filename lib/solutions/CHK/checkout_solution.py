# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus):
    """
    skus = A string containing the SKUs of all the products in the basket
    """
    # Create counters of A's and B's, after summing all variables we reduce
    # using special offers
    as = 0
    bs = 0

    # Create a dictionary of prices
    prices_dict = {"A": 50, "B": 30, "C": 20, "D": 15}

    # Create a total price object:
    price_counter = 0

    # Iterate through the items
    for item in skus:
        if item == "A":
            as += 1
        elif item == "B":
            bs += 1

        price_counter += prices_dict[item]

    # Create A discount:
    as_discount = (as // 3) * (50 * 3 - 130)

    # Create B discount:
    bs_discount = (bs // 2) * (30 * 2 - 45)

    price_counter = price_counter - as_discount - bs_discount

    return(price_counter)
