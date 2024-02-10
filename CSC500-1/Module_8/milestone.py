# Create the shopping_cart class
class shopping_cart:
    def __init__(self):
        # Initialize cart as empty list
        self.cart_items = []
        self.item = self.ItemToPurchase()
        self.customer_name = "none"
        self.current_date = "January 1, 2020"

    def __init__(self, customer_name, current_date):
        # Initialize cart as empty list
        self.cart_items = []
        self.item = self.ItemToPurchase()
        self.customer_name = customer_name
        self.current_date = current_date

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
            self.item_name        = "none"  # string
            self.item_price       = 0.0     # float (prompt said 0, but made float)
            self.item_quantity    = 0       # int
            self.item_description = "none"  # string

        # print total cost of line item per assignment prompt
        def print_item_cost(self):
            self.price_times_qty = self.item_price * self.item_quantity
            print("%s %d @ $%0.2f = $%0.2f" %  (self.item_name,
                                                self.item_quantity,
                                                self.item_price,
                                                self.price_times_qty))

        # print descriptions
        def print_item_description(self):
            self.price_times_qty = self.item_price * self.item_quantity
            print("%s: %s" %  (self.item_name, self.item_description))

    # Add an item to the cart by creating an ItemToPurchase object and appending it to the cart list
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # Remove item method by popping cart index
    def remove_item(self, item_name):
        item_found = False
        for i in range(len(self.cart_items)):
            if item_name in self.cart_items[i].item_name:
                item_found = True
                print("\t%d %s removed from cart." % (self.cart_items[i].item_quantity, self.cart_items[i].item_name))
                self.cart_items.pop(i)
                break
        if not item_found:
            print("\tItem not found in cart. Nothing removed.")
    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    def modify_item(self, ItemToPurchase):
        item_found = False
        for i in range(len(self.cart_items)):
            if ItemToPurchase.item_name in self.cart_items[i].item_name:
                item_found = True
                print("\nItem %s found in cart...Updating..." % ItemToPurchase.item_name)
                self.cart_items[i].print_item_cost()
                print("\tHas been updated to:")
                self.cart_items[i].item_quantity = ItemToPurchase.item_quantity
                self.cart_items[i].print_item_cost()
                break
        if not item_found:
            print("\nItem not found in cart. Nothing modified.")

    # Show cart contents method
    def print_cart_contents(self, what):
        print("-------------------------------------")
        for x in range(len(self.cart_items)):
            print("Item %d: " % (x+1),end="")
            if what == "items":
                self.cart_items[x].print_item_cost()
            elif what == "description":
                self.cart_items[x].print_item_description()
        print("-------------------------------------")

    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        return sum([item.item_quantity for item in self.cart_items])

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        return sum([items.price_times_qty for items in self.cart_items])

    # Outputs total of objects in cart.
    def print_total(self):
        # Check if there are items in the cart
        if 0 < len(self.cart_items):
            print("%s's Shopping Cart - %s" % (self.customer_name, self.current_date))
            print("Number of Items: %d" % self.get_num_items_in_cart())
            # print items in cart
            self.print_cart_contents("items")
            print("Total: $%.2f" % self.get_cost_of_cart())
        else:
            print("\nSHOPPING CART IS EMPTY")

    # Outputs each item's description.
    def print_descriptions(self):
        # Check if there are items in the cart
        if 0 < len(self.cart_items):
            print("%s's Shopping Cart - %s" % (self.customer_name, self.current_date))
            print("Item Descriptions")
            # print items in cart
            self.print_cart_contents("description")
        else:
            print("\nSHOPPING CART IS EMPTY")

    # Checkout method to print goodbye msg
    def checkout(self):
        if (self.get_cost_of_cart() > 0):
            print("\nThank you for shopping with us!")
        else:
            print("\nNothing in your cart, have a nice day!\n")

# Get user input
def print_input():
    print("\nMenu options:")
    print("\ta - Add Item")
    print("\tr - Remove Item")
    print("\tc - Change item quantity")
    print("\ti - Output items' descriptions")
    print("\to - Output shopping cart")
    print("\tq - Quit")
    print("\t=====================================")

    menu_selection = input("\tPlease enter a menu selection and press enter: ")

    # input validation
    try:
        # make sure inputs are from menu list
        if (menu_selection in ["a","r","c","i","o","q"]):
            return menu_selection
        else:
            return print_input()
    except:
        return print_input()

# Init shopping cart object
my_cart = shopping_cart(input("Enter customer's name:\n"), input("Enter today's date:\n"))
print("Customer's name: " + my_cart.customer_name)
print("Today's date: " + my_cart.current_date)

# Shopping loop
checkout = False # loop control variable
while not checkout:

    # Present user with menu until checkout is true
    user_selection = print_input()

    # add or remove items from cart based on user selection, or checkout
    match user_selection:
        case "a":
            new_item = my_cart.ItemToPurchase()
            try:
                print("\nItem", len(my_cart.cart_items) + 1)
                new_item.item_name = str(input("Enter the item name:\n"))
                new_item.item_description = input("Enter the item description:\n")
                new_item.item_price = float(input("Enter the item price:\n"))
                new_item.item_quantity = int(input("Enter the item quantity:\n"))
                print("\nAdded to cart: ",end="")
                new_item.print_item_cost()
                my_cart.add_item(new_item)
            except:
                print("Sorry, item name, price or quantity was not valid, nothing added.")

        case "r":
            print("\nREMOVE ITEM FROM CART")
            # Print curret cart contents to select from
            print("Cart Currently Contains:")
            my_cart.print_cart_contents("items")
            # get user input of name of item to remove
            item_to_remove = input("\nEnter name of item to remove: ")
            my_cart.remove_item(item_to_remove)
        case "c":
            print("\nCHANGE ITEM QUANTITY")
            # Print curret cart contents to select from
            print("Cart Currently Contains:")
            my_cart.print_cart_contents("items")
            # initialize an item to pass to modify_item()
            modified_item = my_cart.ItemToPurchase()
            # get user input of name of item to modify
            print("\nWhich item do you want to modify?")
            modified_item.item_name = str(input("Enter the item name:\n"))
            modified_item.item_quantity = int(input("Enter the new quantity:\n"))
            # Send item update data to modify_item to update cart
            my_cart.modify_item(modified_item)
        case "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            my_cart.print_descriptions()
        case "o":
            print("\nOUTPUT SHOPPING CART")
            my_cart.print_total()
        case "q":
            # end shopping loop
            checkout = True
            # print good bye msg
            my_cart.checkout()
        case _:
            pass
