menue = '''
                     Welcome
                     -------
                  AI PIZZA CAFE
                  -------------
Pizza       |   Large  |   Medium   |  Small  |
-----       |   -----  |   ------   |  -----  |
FAJITA      |   1550   |   775      |  390    | 
CLASSIC     |   1350   |   675      |  340    | 
TIKKA       |   1250   |   625      |  320    |   
AI SPECIAL  |   1750   |   875      |  440    |    
       
COLD DRINKS |  REGULAR |    Medium  |  F.PACK |
----------- |   ------ |    ------  |  ------ |
COCA COLA   |   70     |    110     |  160    |     
PEPSI       |   70     |    110     |  160    |        
SPRITE      |   70     |    110     |  160    |      
            
BURGERS     |   PRICE  |            |         |          
-------     |   -----  |            |         |         
ZINGER      |   200    |            |         |               
PATTY       |   200    |            |         |                
'''
# print(menue)
# lines = menue.splitlines()
# for line in lines:
#     list = line.split()
# print(lines)


lines_list = []

# Iterate through each line of the menue
for line in menue.splitlines():
    # Split the line into words and append them to lines_list
    lines_list.append(line.split())
print(lines_list[5][0])

# Flavours
F,C,T,A=lines_list[7][0],lines_list[8][0],lines_list[9][0],lines_list[10][0]
L,M,S,=lines_list[5][6],lines_list[5][4],lines_list[5][2]
pz =input(f"Select the Flavour (From a,b,c,d):\na){F}\nb){C}\nc){T}\nd){A}\n")


match pz:
    
    
    case 'a':
        print(f"You selected {F} flavor.")
        sz =input(f"\nSelect the Size (From a,b,c):\na){S}\nb){M}\nc){L}\n")
        match sz:
            case 'a':
                print(f"You selected {S} {F}.")
                s=lines_list[7][2]
            case 'b':
                print(f"You selected {M} {F}.")
                s=lines_list[7][4]
            case 'c':
                print(f"You selected {L} {F}.")
                s=lines_list[7][6]
            case _:
                print("Invalid choice. Please select from a, b, c, or d.")
        
        
        
        
    case 'b':
        print(f"You selected {C} flavor.")
        sz =input("\nSelect the Size (From a,b,c):\na)Small\nb)Medium\nc)Large\n")
        match sz:
            case 'a':
                print(f"You selected {S} {C}.")
                s=lines_list[8][2]
            case 'b':
                print(f"You selected {M} {C}.")
                s=lines_list[8][4]
            case 'c':
                print(f"You selected {L} {C}.")
                s=lines_list[8][6]
            case _:
                print("Invalid choice. Please select from a, b, c, or d.")
                
    
                
    case 'c':
        print(f"You selected {T} flavor.")
        sz =input("\nSelect the Size (From a,b,c):\na)Small\nb)Medium\nc)Large\n")
        match sz:
            case 'a':
                s=lines_list[9][2]
                print(f"You selected {S} {T}.")
            case 'b':
                print(f"You selected {M} {T}.")
                s=lines_list[9][4]
            case 'c':
                print(f"You selected {L} {T}.")
                s=lines_list[9][6]
            case _:
                print("Invalid choice. Please select from a, b, c, or d.")
       
                
                
    case 'd':
        print(f"You selected {A} flavor.")
        sz =input("\nSelect the Size (From a,b,c):\na)Small\nb)Medium\nc)Large\n")
        match sz:
            case 'a':
                print(f"You selected {S} {A}.")
                s=lines_list[10][2]
            case 'b':
                print(f"You selected {M} {A}.")
                s=lines_list[10][4]
            case 'c':
                print(f"You selected {L} {A}.")
                s=lines_list[10][6]
            case _:
                print("Invalid choice. Please select from a, b, c, or d.")
    case _:
        print("Invalid choice. Please select from a, b, c, or d.")
n=int(input("Enter the quantity of Pizza (numbers):"))
pizza=n*int(s)
print(f"Your bill = {pizza}")