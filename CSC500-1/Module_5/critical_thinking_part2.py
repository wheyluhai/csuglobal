# Get number of books
def get_books():
    num_books = input("\nPlease enter the number of books you have purchased this month and press enter: ")
    # guard for invalid entries
    try:
        if not num_books.isnumeric():
            print("\nPlease enter an integer.")
            return get_books()
        num_books = int(num_books)
    except:
        print("\nPlease enter an integer.")
        return get_books()
    return num_books

# Init rewards values
points_categories = {0:0, 2:5, 4:15, 6:30, 8:60}

# Init rewards to 0
rewards_pts = 0

# Get user book purchases
num_books_this_month = get_books()

# Iterate through rewards levels
for tier in points_categories:
    # if books purchased is greater or equal to current tier set corresponding rewards points
    if num_books_this_month >= tier:
        rewards_pts = points_categories[tier]
    else:
        break

if rewards_pts == 0:
    print("\nPlease purchase at least 2 books a month to receive rewards points!")
else:
    print("\nCongratulations! You've received %d rewards points this month!" % rewards_pts)
