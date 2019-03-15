for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
n = int(input("enter a number"))
single_line_stars = n * "*"
print(single_line_stars)

#d
loop_counter = int(0)

while loop_counter < n:
    loop_counter += 1
    multi_line_stars = loop_counter * "*"
    print(multi_line_stars)
