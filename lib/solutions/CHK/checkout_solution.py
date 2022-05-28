def checkout(skus):
    """
    skus = A string containing the SKUs of all the products in the basket

    Applies the following prices and special offers and returns the total price
    at checkout:

    +------+-------+---------------------------------+
    | Item | Price | Special offers                  |
    +------+-------+---------------------------------+
    | A    | 50    | 3A for 130, 5A for 200          |
    | B    | 30    | 2B for 45                       |
    | C    | 20    |                                 |
    | D    | 15    |                                 |
    | E    | 40    | 2E get one B free               |
    | F    | 10    | 2F get one F free               |
    | G    | 20    |                                 |
    | H    | 10    | 5H for 45, 10H for 80           |
    | I    | 35    |                                 |
    | J    | 60    |                                 |
    | K    | 70    | 2K for 120                      |
    | L    | 90    |                                 |
    | M    | 15    |                                 |
    | N    | 40    | 3N get one M free               |
    | O    | 10    |                                 |
    | P    | 50    | 5P for 200                      |
    | Q    | 30    | 3Q for 80                       |
    | R    | 50    | 3R get one Q free               |
    | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | U    | 40    | 3U get one U free               |
    | V    | 50    | 2V for 90, 3V for 130           |
    | W    | 20    |                                 |
    | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
    +------+-------+---------------------------------+
    """
    # Type checks
    if type(skus) != str:
        return -1

    # Create counters dictionary of special items. After summing all prices we reduce
    # the checkout using special offers

    special_counts = {"A": 0, "B": 0, "E": 0, "F": 0, "H": 0, "K": 0, "M": 0,
                      "N": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0,
                      "V": 0, "X": 0, "Y": 0, "Z": 0}

    special_discounts = {k: v for k, v in special_counts.items()}


    # Create a dictionary of prices
    prices_dict =  {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20,
                    "H": 10, "I": 35, "J": 60, "K": 70, "L": 90, "M": 15, "N": 40,
                    "O": 10, "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20, "U": 40,
                    "V": 50, "W": 20, "X": 17, "Y": 20, "Z": 21}



    # Create a total price object:
    price_counter = 0

    # Iterate through the items adding the individual prices
    for item in skus:
        # For non-implemented itemsType check:
        if item not in prices_dict.keys():
            return -1
        elif item in special_counts:
            special_counts[item] += 1

        price_counter += prices_dict[item]

    # --- INDIVIDUAL DISCOUNTS BEGINNING

    # Create A discount:
    a_discount_by_5 = (special_counts["A"] // 5) * (prices_dict["A"] * 5 - 200)
    remainder_after_5 = special_counts["A"] % 5
    a_discount_by_3 = (remainder_after_5 // 3) * (prices_dict["A"] * 3 - 130)
    special_discounts["A"] = a_discount_by_5 + a_discount_by_3

    # Apply E discount to B (Here I assume that we remove all B's that have been free)
    b_free = special_counts["E"] // 2
    special_discounts["B"] = min(special_counts["B"], b_free) * prices_dict["B"]

    # --- Substract those items that have been free
    special_counts["B"] -= min(special_counts["B"], b_free)

    # Create B discount to the remaining non-free B's:
    special_discounts["B"] += (special_counts["B"] // 2) * (prices_dict["B"] * 2 - 45)

    # Apply F discount:
    # Every three, because you don't pay for the third one and it doesn't count
    # for the new discount either
    # In other words, out of every three, one is free
    f_free = (special_counts["F"] // 3)
    special_discounts["F"] = f_free * prices_dict["F"]

    # Create H discount
    h_discount_by_10 = (special_counts["H"] // 10) * (prices_dict["H"] * 10 - 80)
    remainder_after_10 = special_counts["H"] % 10
    h_discount_by_5 = (remainder_after_10 // 5) * (prices_dict["H"] * 5 - 45)
    special_discounts["H"] = h_discount_by_10 + h_discount_by_5

    # Create K discount:
    special_discounts["K"] = (special_counts["K"] // 2) * (prices_dict["K"] * 2 - 120)

    # Create N discount for M:
    m_free = special_counts["N"] // 3
    special_discounts["M"] = min(special_counts["M"], m_free) * prices_dict["M"]

    # Create P discount:
    special_discounts["P"] = (special_counts["P"] // 5) * (prices_dict["P"] * 5 - 200)

    # Create R discount for Q
    q_free = special_counts["R"] // 3
    special_discounts["Q"] = min(special_counts["Q"], q_free) * prices_dict["Q"]

    # --- Substract those items that have been free
    special_counts["Q"] -= min(special_counts["Q"], q_free)

    # Create Q discount:
    special_discounts["Q"] += (special_counts["Q"] // 3) * (prices_dict["Q"] * 3 - 80)

    # Create U discount:
    u_free = special_counts["U"] // 4
    special_discounts["U"] = u_free * prices_dict["U"]

    # Create V discount:
    v_discount_by_3 = (special_counts["V"] // 3) * (prices_dict["V"] * 3 - 130)
    remainder_after_3 = special_counts["V"] % 3
    v_discount_by_2 = (remainder_after_3 // 2) * (prices_dict["V"] * 2 - 90)
    special_discounts["V"] = v_discount_by_2 + v_discount_by_3

    # --- GROUP DISCOUNTS BEGINNING:

    # Use the labels to get their prices and counts
    # Items with higher prices will be discounted first
    # Group counts will be eliminated in the discount loop
    group_labels = ["S", "T", "X", "Y", "Z"]
    group_prices = {label: price for label, price in prices_dict.items()
                    if label in group_labels}
    group_counts = {label: count for label, count in special_counts.items()
                    if label in group_labels}

    sort_prices = sorted(group_prices.items(), key = lambda item: item[1], reverse = True)

    # Total discounts (used later) and number of items with discount (as a counter
    # for a while loop)
    n_group_discounts = sum(group_counts.values()) // 3
    n_items_with_discount = n_group_discounts * 3

    #print("group discounts", n_group_discounts)

    while n_items_with_discount > 0:
        # From the most expensive items to the cheapest ones, take their prices out of
        # the price counter
        for item in sort_prices:
            # If an item discount has not been applied to all of its units, take one of its units
            # substract its price from the total price counter, and take one item out of
            # the total number of items with discount. Then break the loop to check
            # that we have not reached the maximum number of items with discount

            if group_counts[item[0]] > 0:
                group_counts[item[0]] -= 1 # - 1 item of this certain label
                price_counter -= item[1]   # Take price out
                n_items_with_discount -= 1 # -1 item with discount
                break

            # If the item is depleted, go to the next one
            else:
                continue

    # --- GROUP DISCOUNTS ENDING

    individual_discounts = sum(special_discounts.values())

    # Add the price of total group discounts
    price_counter = price_counter + n_group_discounts * 45 - individual_discounts

    return(price_counter)

