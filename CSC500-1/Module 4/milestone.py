# Create the shopping_cart class
class shopping_cart:

    def __init__(self):
        # Initialize cart as empty list
        self.cart = []
        self.item = self.ItemToPurchase()

    # Step 1: Build the ItemToPurchase class with the following specifications:
    #         - item_name (string)
    #         - item_price (float)
    #         - item_quantity (int)
    #         Default constructor Initializes item's
    #         - name = "none"
    #         - item's price = 0
    #         - item's quantity = 0
    #         Method
    #         - print_item_cost()
    # Create the ItemToPurchase class
    class ItemToPurchase:

        # Default constructor no parameters per assignment prompt
        def __init__(self):
            self.item_name     = "none"  # string
            self.item_price    = 0.0     # float (prompt said 0, but made float)
            self.item_quantity = 0       # int

        # print total cost of line item per assignment prompt
        def print_item_cost(self):
            self.price_times_qty = self.item_price * self.item_quantity
            print("%s %d @ $%0.2f = $%0.2f" %  (self.item_name,
                                                self.item_quantity,
                                                self.item_price,
                                                self.price_times_qty))

    # Add an item to the cart by creating an ItemToPurchase object and appending it to the cart list
    def add_item(self):
        self.cart.append(self.ItemToPurchase())

        # Skipping input validation for simplicity
        #    If user enters a string (non number) into item price or quantity the program will crash
        print("\nItem", len(self.cart))
        self.cart[-1].item_name = str(input("Enter the item name:\n"))
        self.cart[-1].item_price = float(input("Enter the item price:\n"))
        self.cart[-1].item_quantity = int(input("Enter the item quantity:\n"))
        print("Added to cart: ",end="")
        self.cart[-1].print_item_cost()

    # Remove item method by popping cart index
    def remove_item(self):
        self.show_cart()
        item_to_remove = int(input("\nWhich item do you want to remove? (Enter Item number): ")) - 1

        if item_to_remove in range(len(self.cart)):
            print("\t%d %s removed from cart." % (self.cart[item_to_remove].item_quantity, self.cart[item_to_remove].item_name))
            self.cart.pop(item_to_remove)
        else:
            print("\tItem number not valid.")
            return self.remove_item()

    # Show cart contents method
    def show_cart(self):
        print("\nCart Contains:")
        print("\t-------------------------------------")
        for x in range(len(self.cart)):
            print("\tItem %d: " % (x+1),end="")
            self.cart[x].print_item_cost()
        print("\t-------------------------------------")

    # Calculate total cost of shopping cart method
    def get_cart_total(self):
        return sum([items.price_times_qty for items in self.cart])

    # Checkout method
    def checkout(self):
        self.total = self.get_cart_total()

        # Step 3: Add the costs of the two items together and output the total cost
        if (self.total > 0):
            print("\nTOTAL COST")
            print("-------------------------------------")
            for items in self.cart:
                items.print_item_cost()
            print("-------------------------------------")
            print("Total: $%.2f\n" % self.total)
            print("Thank you for shopping with us!")
        else:
            print("\nNothing in your cart, have a nice day!")

# Get user input
def get_input():
    print("\nMenu options:")
    print("\t1. Add Item")
    print("\t2. Remove Item")
    print("\t3. Checkout")
    print("\t=====================================")

    menu_selection = input("\tPlease enter a number (1-3) and press enter: ")

    # input validation
    try:
        menu_selection = int(menu_selection)
        if (1 <= menu_selection and menu_selection <= 3):
            return menu_selection
        else:
            return get_input()
    except:
        return get_input()


# Init shopping cart object
my_cart = shopping_cart()

# Shopping loop
checkout = False # loop control variable
while not checkout:
    user_selection = get_input()

    # add or remove items from cart based on user selection, or checkout
    match user_selection:
        case 1:
            my_cart.add_item()
        case 2:
            my_cart.remove_item()
        case 3:
            checkout = True
            my_cart.checkout()
        case _:
            pass
