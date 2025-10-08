'''
Name: Sonboleh Mousavi
Team Name: Hungry Python
Team Members:       Sonya Hu, Sonboleh Mousavi, Khadija Masri

Description:
Provide user a menu to order from.  Save the selection and return the bill with
details on each order, tax amount and amount due.
'''
from cafe import Order

if __name__ == "__main__":
    flag = True
    order = Order() # one order to reuse for whole session
    while flag:
        order.display_menu()
        my_order, the_count = order.get_inputs()
        total = order.calculate(my_order, the_count)
        payment_with_tax = order.bill(my_order, the_count, total)
        order.save(my_order, the_count, total, payment_with_tax)

        to_continue = input("Do you wish to continue? any key for yes and No for no")
        if to_continue.lower() == "no":
            print("Exiting....")
            flag = False


'''
1. add a try/except         Sonya
2. Add a child class        khadija
3. Do you wish to continue, wipes everything clean.  Sonya

Outputs:

Here is the menu at De Anza College:  
0:  De Anza Burger  price: 5.25
1:  Bacon Cheese  price: 5.75
2:  Mushroom Swiss  price: 5.95
3:  Western Burger  price: 5.95
4:  Don Cali Burger  price: 5.95
Enter your desired item(0-4). Enter 6 to exit the menu. 1
How many Bacon Cheese are you interested to purchase? 2
Sum is 11.50.
Are you a staff member? Enter Yes or No^Z
[8]+  Stopped                 python3 deanza.py
sonyah939@HungryCat:/mnt/c/Users/angel/Downloads/python/Advanced$ python3 deanza.py
Here is the menu at De Anza College:  
0:  De Anza Burger  price: 5.25
1:  Bacon Cheese  price: 5.75
2:  Mushroom Swiss  price: 5.95
3:  Western Burger  price: 5.95
4:  Don Cali Burger  price: 5.95
Enter your desired item(0-4). Enter 6 to exit the menu. 2
How many Mushroom Swiss are you interested to purchase? 1
Enter your desired item(0-4). Enter 6 to exit the menu. 3
How many Western Burger are you interested to purchase? 2
Enter your desired item(0-4). Enter 6 to exit the menu. -1
Please enter a valid input between 0-4, or 6 to exit.
Enter your desired item(0-4). Enter 6 to exit the menu. 5
Please enter a valid input between 0-4, or 6 to exit.
Enter your desired item(0-4). Enter 6 to exit the menu. 4
How many Don Cali Burger are you interested to purchase? -1
Please enter a positive number.
How many Don Cali Burger are you interested to purchase? 1
Enter your desired item(0-4). Enter 6 to exit the menu. 6
Thank you for your order.
Sum is 23.80.
Are you a staff member? Enter Yes or NoNo
------------------
You ordered:
------------------
1 X Mushroom Swiss  @  5.95
2 X Western Burger  @  5.95
1 X Don Cali Burger  @  5.95
Total before tax: 23.80
Tax:    0.00
Total after tax:  23.80
Do you wish to continue? any key for yes and No for nono
Exiting....

'''
