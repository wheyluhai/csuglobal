# Part 1:
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

import random

# Get number of years
def get_years():
    years = input("Please enter the number of years of data you will provide and press enter: ")
    # guard for invalid entries
    try:
        if not years.isnumeric():
            print("\nPlease enter an integer.")
            return get_years()
        years = int(years)
    except:
        print("\nPlease enter an integer.")
        return get_years()
    return years

# Get rainfall
def get_rainfall(year, month):
    rainfall = input("Please enter rainfall (inches) for Year %d %s and press enter: " % (year, month))
    # guard for invalid entries
    try:
        rainfall = float(rainfall)
    except:
        print("\nPlease enter a number.")
        return get_rainfall(year, month)
    return rainfall

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"  ]

# init rainfall list
rainfall = []

# First loop (years)
# get years
num_years = get_years()
for i in range(num_years):
    # Second loop (months)
    for month in months:
        rainfall.append(get_rainfall(i+1, month))

print("\nTotal number of months of data collected: %d" % len(rainfall))
print("\nThe average rainfall in inches per month for this period was: %0.2f in\n" % (sum(rainfall)/len(rainfall)))
