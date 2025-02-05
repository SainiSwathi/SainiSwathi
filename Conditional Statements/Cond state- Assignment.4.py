#4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount. 
#battery-based-more than 1000rs order -10% discount.
#key-based toys -more than 100 order - 5% discount
#Eletrical-based toys -more than 500 order -10% dis

#product code & order amount
#Net amount after discount = ?

Toys=int(input("Enter the toys Battery-based, Key-based, Electrical-based): "))
Product_code=int(input("Enter the product_code (1, 2, 3): "))
order_amount=float(input("Enter the order amount: "))
if Product_code == 1 and order_amount > 1000: 
    discount = 0.10 * oder_amount #10% =0.10
if Product_code == 2 and order_amount > 100:
    discount = 0.05 * order_amount#5% =0.05
if Product_code == 3 and order_amount > 500:
    discount = 0.10 * order_amount#10% =0.10
else:
    discount = 0.00
net_amount = order_amount - (order_amount * discount)
print(f"net_amount to be paid: Rs. {net_amount}")
