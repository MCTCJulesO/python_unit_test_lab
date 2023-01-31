def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    # This checks if a list is at least 3 items long
    # If the list is shorter than 3 items, 0 will be returned
    if len(item_prices) >= 3:
        return min(item_prices)
    else:
        return 0


if __name__ == '__main__':
    main()