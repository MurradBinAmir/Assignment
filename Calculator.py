#Calculator only using variables, Input & Conditions
op   = str(input("Enter only one operator from '+, -, *, /' : "))
# when learn loops,
# I can enter while loop to check operator is correct,
# instaed of runing whole program or taking user input
var  = int(input("Enter number 1 :"))
var1 = int(input("Enter number 2 :"))
print("\nAnswer :", end="")
if(op == "+"):
    print(f"{var} + {var1} = {var+var1}")
if(op == "-"):
    print(f"{var} - {var1} = {var-var1}")
if(op == "*"):
    print(f"{var} * {var1} = {var*var1}")
if(op == "/"):
    if(var1==0):
        print(f"can not divide {var} by {var1}")
    else:
        # use float for output in points
        print(f"{var} / {var1} = {float(var/var1)}",f"Remainder of {var} / {var1} is {var%var1}",sep="\n")
else:
    print("Invalid operator. Please enter '+', '-', '*', or '/'")
print(
'''
Good Bye if you get your Answer
Come back if you want more Answers
''')
