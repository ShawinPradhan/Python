# Function to calculate the net amount after applying discounts
def calculate_discounted_amount(product_code, order_amount):
    discount = 0
    if product_code == 1 and order_amount > 1000:
        discount = 0.1 * order_amount
    elif product_code == 2 and order_amount > 100:
        discount = 0.05 * order_amount
    elif product_code == 3 and order_amount > 500:
        discount = 0.1 * order_amount

    net_amount = order_amount - discount
    return net_amount

# Input product code and order amount from the user
print("1 for Battery Based Toys\n2 for Key-based Toys\n"
      "3 for Electrical Charging Based Toys")
product_code = int(input("Enter the product code : "))
order_amount = float(input("Enter the order amount in Rs.: "))

# Calculate the net amount after applying discounts
net_amount = calculate_discounted_amount(product_code, order_amount)

# Display the net amount
print(f"Net amount after applying discount: Rs. {net_amount:.2f}")


##OUTPUT
##1 for Battery Based Toys
##2 for Key-based Toys
##3 for Electrical Charging Based Toys
##Enter the product code : 2
##Enter the order amount in Rs.: 300
##Net amount after applying discount: Rs. 285.00
