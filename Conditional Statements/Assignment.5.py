print("\nToy Types:")
print("1:Battery Based Toy")
print("2:Key Based Toy")
print("3:Electric Based Toy")
toy_type=int(input("Enter the product code(1,2,3): "))
order_amount=float(input("Enter the order amount"))

if toy_type == 1 and order_amount > 1000:
    discount = 0.10 * order_amount
if toy_type == 2 and order_amount > 100:
    discount = 0.05 * order_amount
if toy_type == 3 and order_amount > 500:
    discount = 0.10 * order_amount
else:
    discount = 0
net_amount = order_amount - discount
print(f"net_amount to be paid: Rs. {net_amount}")
                         
                         

                         
