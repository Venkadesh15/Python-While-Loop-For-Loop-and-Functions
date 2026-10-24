# 2) Multiplication Table Generator using For Loop

# 2.1) GETTING INPUT FROM THE USER
number = int(input("Enter the number for which you want the multiplication table: "))
# 2.2) USING FOR LOOP
for i in range(1, 11): 
# 2.3) CALCULATING THE RESULT
    result = number * i
# 2.4) PRINTING THE MULTIPLICATION TABLE
    print(f"{number} x {i} = {result}")