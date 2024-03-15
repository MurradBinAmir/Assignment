import numpy as np

# n number of fabonachi
# using for loop
n = int(input("Using for loop \nenter number to get fabonachi till  that number :"))
# # starting numbers
# f_numbers=[0,1]
# for _ in range(n - 2):
#     # negative index use kr ka next Fibonacci number find krayn ga
#     next_fibonacci = f_numbers[-1] + f_numbers[-2]
#     # list ma store krayn ga
#     f_numbers.append(next_fibonacci) 
# f_numbers.pop(1)   
# print(f_numbers)





#Q1 Using while loop
print("using while loop\n")
f_numbers = [0, 1]
while len(f_numbers) < n:
    next_fibonacci = f_numbers[-1] + f_numbers[-2]
    f_numbers.append(next_fibonacci)
f_numbers.pop(1)
print(f_numbers)


#Q2  n number of factorial
factorial = 1
# 1 sa la ka us iteration wala number tak
for i in range(n):
    # for number sa 1 pahla tak chalta ha, to i+1
    factorial = factorial*(i+1)
print(f"Factorial of {i}: {factorial}")



#Q3 unpack tuple , print in reverse order
tuple = (1, 2, 3, 4, 5)
array = np.array(tuple)
print(f"tuple before reversing {tuple}")
tuple=array[::-1]
print(f"tuple after reversing :{tuple}")