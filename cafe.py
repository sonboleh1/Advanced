from arraybag import ArrayBag
from datetime import datetime

MENU = ["De Anza Burger", "Bacon Cheese", "Mushroom Swiss", "Western Burger", "Don Cali Burger"]
PRICE =[5.25, 5.75, 5.95, 5.95, 5.95]
FILENAME = "bill.txt"

class Order():
    '''
    Choose items to order, clear the order or edit the order or cancel the order.
    Once done, calculate the price before tax and after tax for a student/faculty member
    or for the general public
    '''

    def __init__(self):
        self.display = ArrayBag(MENU)
        self.mybag = ArrayBag()
        self.mycount = ArrayBag()

    def display_menu(self):
        '''
        Display the food menu
        '''
        print(f"Here is the menu at De Anza College:  ")
        i = 0
        for item in self.display:
            print(f"{i}:  {item}  price: {PRICE[i]}")
            i +=1

    def get_inputs(self):
        '''
        Get user input.  There are 5 items on the menu and 6 is to exit the menu.
        '''

        item = int(input(f"Enter your desired item(0-4). Enter 6 to exit the menu. "))
        if item == 6:
            print("Thank you for your order.")
        elif item >= 0 and item < 5:
            count = int(input(f"How many are you interested to purchase? "))

        while item != 6:
            if item >= 0 and item < 5:
                #for i in range(count):
                self.mybag.add(item)
                self.mycount.add(count)

            item = int(input(f"Enter your desired item(0-4). Enter 6 to exit the menu "))
            if item == 6:
                print("Thank you for your order.")
            elif item >= 0 and item < 5:
                count = int(input(f"How many {MENU[item]} are you interested to purchase? "))
                #print(f"{count} X {MENU[item]}")

        return self.mybag, self.mycount

    def is_staff(self):
        '''
        Check if the customer is a staff member or a student.
        '''
        role = input(f"Are you a staff member? Enter Yes or No")
        return role.lower() == "yes"


    def calculate(self, selection, the_count):
        '''
        Calculate the sum of order
        '''
        subtotal = 0
        for item1, item2 in zip(selection, the_count):
            subtotal += PRICE[item1] * item2

        print(f"Sum is {subtotal:.2f}. ")

        return subtotal

    def bill(self, selection, the_count, subtotal):
        '''
        Print the bill inluding, food items and quantities, cost of each item,
        tax and total before and after tax.
        '''
        tax = 0
        if self.is_staff():
            # add 9% tax
            tax += subtotal * 0.09

        # Print bill
        print("------------------")
        print("You ordered:")
        print("------------------")
        for item1, item2 in zip(the_count, selection):
            print(f"{item1} X {MENU[item2]}  @  {PRICE[item2]}")

        print(f"Total before tax: {subtotal:.2f}")
        print(f"Tax:\t{tax:.2f}")

        total = subtotal + tax
        print(f"Total after tax:  {total:.2f}")

        return total

    # write  a function to copy all of these to a file 
    def save(self, selection, the_count, subtotal, total):
        '''
        Save the order to a file
        Include what was ordered, its count and total before tax and after tax
        '''

        current_time = datetime.now().strftime("%Y-%m-%d")
        # Write to the file
        with open(FILENAME, "w") as f:
            f.write(f"Todays date:    {current_time}")
            f.write("\n\n\n")
            for item1, item2 in zip(the_count, selection):
                f.write(f"{item1} X {MENU[item2]} @  {PRICE[item2]} \n")

            f.write(f"Total before tax: {subtotal:.2f} \n")
            f.write(f"Tax: {total-subtotal:.2f} \n")
            f.write(f"Total after tax:  {total:.2f} \n")


    # write a class to re-order 
    # class Reorder(Order):
    
