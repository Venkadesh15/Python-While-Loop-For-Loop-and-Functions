
# 3) BMI Calculator

# 3.1) DEFINING THE FUNCTION
def calculate_bmi(weight, height):
# 3.2) CALCULATING THE RESULT
    bmi = weight / (height ** 2)
# 3.3) RETURNING THE RESULT
    return bmi
# 3.4) GETTING WEIGHT FROM THE USER
weight = float(input("Enter your weight in kg: "))
# 3.5) GETTING HEIGHT FROM THE USER
height = float(input("Enter your height in meters: "))
# 3.6) CALLING THE FUNCTION
bmi = calculate_bmi(weight, height)
# 3.7) DISPLAYING THE BMI
print(f"Your BMI is: {bmi:.2f}")
