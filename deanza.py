'''
Name: Sonboleh Mousavi
Team Name: Hungry Python
Team Members:       Sonya Hu, Sonboleh Mousavi, Khadija Masri

Description:
Provide user a menu to order from.  Save the selection and return the bill with
details on each order, tax amount and amount due.
'''
from cafe import Order
from cafe import StaffOrder, StudentOrder

if __name__ == "__main__":
    flag = True
    order = Order() # one order to reuse for whole session
    role = ""
    while role != "yes" and role != "no":
        role = input("Are you a staff member? Enter Yes or No: ").strip().lower()

    while flag:
        order.display_menu()
        my_order, the_count = order.get_inputs()
        total = order.calculate(my_order, the_count)
        payment_with_tax = order.bill(my_order, the_count, total, role)
        order.save(my_order, the_count, total, payment_with_tax)

        to_continue = input("Do you wish to continue? any key for yes and No for no")
        if to_continue.lower() == "no":
            print("Exiting....")
            flag = False

'''
Outputs:

Are you a staff member? Enter Yes or No: yes
Here is the menu at De Anza College:
0:  De Anza Burger  price: 5.25
1:  Bacon Cheese  price: 5.75
2:  Mushroom Swiss  price: 5.95
3:  Western Burger  price: 5.95
4:  Don Cali Burger  price: 5.95
Enter your desired item(0-4). Enter 6 to exit the menu. 4
How many Don Cali Burger are you interested to purchase? 1
Enter your desired item(0-4). Enter 6 to exit the menu. 3
How many Western Burger are you interested to purchase? 2
Enter your desired item(0-4). Enter 6 to exit the menu. 6
Thank you for your order.
Tax is 1.6065 and tax rate is 0.09
------------------
You ordered:
------------------
1 X Don Cali Burger  @  5.95
2 X Western Burger  @  5.95
Total before tax: 17.85
Tax:    1.61
Total after tax:  19.46
Do you wish to continue? any key for yes and No for nono
Exiting....
[Finished in 21.8s]

Negative testing:


Are you a staff member? Enter Yes or No: 7
Are you a staff member? Enter Yes or No: xyz
Are you a staff member? Enter Yes or No: no
Here is the menu at De Anza College:
0:  De Anza Burger  price: 5.25
1:  Bacon Cheese  price: 5.75
2:  Mushroom Swiss  price: 5.95
3:  Western Burger  price: 5.95
4:  Don Cali Burger  price: 5.95
Enter your desired item(0-4). Enter 6 to exit the menu. 0
How many De Anza Burger are you interested to purchase? 1
Enter your desired item(0-4). Enter 6 to exit the menu. 1
How many Bacon Cheese are you interested to purchase? 2
Enter your desired item(0-4). Enter 6 to exit the menu. 5
Please enter a valid input between 0-4, or 6 to exit.
Enter your desired item(0-4). Enter 6 to exit the menu. 4
How many Don Cali Burger are you interested to purchase? 10
Enter your desired item(0-4). Enter 6 to exit the menu. 6
Thank you for your order.
Tax is 0.0 and tax rate is 0.0
------------------
You ordered:
------------------
1 X De Anza Burger  @  5.25
2 X Bacon Cheese  @  5.75
10 X Don Cali Burger  @  5.95
Total before tax: 76.25
Tax:    0.00
Total after tax:  76.25
Do you wish to continue? any key for yes and No for noyes
Here is the menu at De Anza College:
0:  De Anza Burger  price: 5.25
1:  Bacon Cheese  price: 5.75
2:  Mushroom Swiss  price: 5.95
3:  Western Burger  price: 5.95
4:  Don Cali Burger  price: 5.95
Enter your desired item(0-4). Enter 6 to exit the menu. 3
How many Western Burger are you interested to purchase? 2
Enter your desired item(0-4). Enter 6 to exit the menu. 6
Thank you for your order.
Tax is 0.0 and tax rate is 0.0
------------------
You ordered:
------------------
1 X De Anza Burger  @  5.25
2 X Bacon Cheese  @  5.75
10 X Don Cali Burger  @  5.95
2 X Western Burger  @  5.95
Total before tax: 88.15
Tax:    0.00
Total after tax:  88.15
Do you wish to continue? any key for yes and No for nono
Exiting....
[Finished in 39.6s]

'''
