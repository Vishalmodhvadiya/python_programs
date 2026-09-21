# Write a program that takes percentage discount on product as input and returns the discounted price of product. Make sure that discount money cannot be less than zero and greater than original price of product using assertion.

def product_discount(price, discount):
    discount = (discount / 100) * price;

    assert discount >= 0, "Discount cannot be less than zero"
    assert discount <= price, "Discount cannot be greater than the original price"

    discounted_price = price - discount
    return discounted_price


price = float(input("Enter the price of the product: "))
discount = float(input("Enter the discount percentage: "))

try:
    final_price = product_discount(price, discount)
    print(f"The final price after discount is: {final_price}")
except AssertionError as e:
    print(f"Error: {e}")

    
    