# Exercise 3: List Iteration
# Apply the function to a list:

# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

def print_factor(x):
    for i in range(1,x+1):
        if x % i ==0:
            print(i)
for number in l:
    print(f"Factors of {number}:")
    print_factor(number)