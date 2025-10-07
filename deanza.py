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
    while flag:
        order = Order()
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


'''
