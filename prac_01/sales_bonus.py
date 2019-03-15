"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(1)
while sales >= 0:
    sales = float(input("Enter sales: $"))
    bonus_percentage = 0
    if sales < 1000:
        bonus_percentage = 0.1
    elif sales >= 1000:
        bonus_percentage = 0.15
    
    bonus = sales * bonus_percentage
    print(bonus)
