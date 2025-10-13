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

    def tax_rate(self) -> int:
        return 0

    def is_staff(self) -> bool:
        return self.tax_rate() > 0
        
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
        while True:
            try:
                item = int(input(f"Enter your desired item(0-4). Enter 6 to exit the menu. "))
            except ValueError:
                print("please enter a numeric input.")
                continue
            if item == 6:
                print("Thank you for your order.")
                break # end loop
            elif 0 <= item <= 4:
                while True:
                    try:
                        count = int(input(f"How many {MENU[item]} are you interested to purchase? "))
                        if count <= 0:
                            print("Please enter a positive number.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid numeric count")
                self.mybag.add(item)
                self.mycount.add(count)
            else:
                print("Please enter a valid input between 0-4, or 6 to exit.")
        return self.mybag, self.mycount

    def calculate(self, selection, the_count):
        '''
        Calculate the sum of order
        '''
        subtotal = 0
        for item, count in zip(selection, the_count):
            subtotal += PRICE[item] * count

        return subtotal

    def bill(self, selection, the_count, subtotal, role):
        '''
        Print the bill inluding, food items and quantities, cost of each item,
        tax and total before and after tax.
        '''
        if role == "yes":
            tax_rate = StaffOrder().tax_rate()
        else:
            tax_rate = StudentOrder().tax_rate()
        tax = subtotal * tax_rate
        print(f'Tax is {tax} and tax rate is {tax_rate}')


        # Print bill
        print("------------------")
        print("You ordered:")
        print("------------------")
        for item, count in zip(selection, the_count):
            print(f"{count} X {MENU[item]}  @  {PRICE[item]}")

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
            for item, count in zip(selection, the_count):
                f.write(f"{count} X {MENU[item]} @  {PRICE[item]} \n")

            f.write(f"Total before tax: {subtotal:.2f} \n")
            f.write(f"Tax: {total-subtotal:.2f} \n")
            f.write(f"Total after tax:  {total:.2f} \n")

class StudentOrder(Order):
    def tax_rate(self) -> int:
        return 0.0

class StaffOrder(Order):
    def tax_rate(self) -> int:
        return 0.09


