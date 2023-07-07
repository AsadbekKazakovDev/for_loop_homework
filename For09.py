def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    ans=[]
    for i in range(1,11):
        ans.append(price*i)
    return ans
price = 2.25
print(main(price))