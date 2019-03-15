

number_of_items = int((input("Enter the number of items:")))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int((input("Enter the number of items:")))

item_list = []

while len(item_list) < number_of_items:
    item_value = float(input("Enter value of item"))
    item_list.append(item_value)


total_value = sum(item_list)
if total_value > 100:
    total_value *= 0.9

print("Total price price for", number_of_items, "items is", "${:.2f} ".format(total_value))
