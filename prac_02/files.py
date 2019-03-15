
user_name = input("Please enter your name:")

name_file = open("name.txt", 'w')
print(user_name, file=name_file)
name_file.close()


name_file = open("name.txt", 'r')
stored_name = name_file.read()
print("Your Name is: {}".format(stored_name))

number_file = open("numbers.txt", 'r')
numbers = number_file.readlines()
number_list = []
for i in numbers:
    number_list.append(int(i))

print(sum(number_list))
