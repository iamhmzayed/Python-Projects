#Project_1 : BODY MASS INDEX (BMI)

a = input("What is your name ? ")
input ("What is your age ? ")
print (f"Welcome {a} Lets check Your BMI")
print("...................................")

Height = float(input("Enter height in centimeter: "))
weight = float(input("Enter weight in kilogram: "))

Height = Height / 100

BMI = weight / (Height * Height)
print(f"\n{a} Your BMI is {BMI: .2f}")

if BMI <=18.4:

    target_weight = 18.4 * (Height * Height)
    weight_diff = target_weight - weight
    if weight_diff > 0:
        print(f"{a} You need to gain {weight_diff:.2f} kg to reach the perfect BMI of {18.5}.")

    elif weight_diff < 0:
        print(f"{a} You need to lose {abs(weight_diff):.2f} kg to reach the perfect BMI of {18.5}.")
    else:
        print(f"{a} You are already at the perfect BMI.")
    print(f"{a} Your are underweight")


elif BMI <= 24.9:
    print(f"{a} Your are Normal. GOOD JOB ")


elif BMI <= 39.9:

    target_weight = 24.9 * (Height * Height)
    weight_diff = target_weight - weight
    if weight_diff > 0:
        print(f"{a} You need to gain {weight_diff:.2f} kg to reach the perfect BMI of {24.9}.")

    elif weight_diff < 0:
        print(f"{a} You need to lose {abs(weight_diff):.2f} kg to reach the perfect BMI of {24.9}.")
    else:
        print(f"{a} You are already at the perfect BMI.")

    print(f"{a} Your are overweight")


else:

    target_weight = 24.9 * (Height * Height)
    weight_diff = target_weight - weight
    if weight_diff > 0:
        print(f"{a} You need to gain {weight_diff:.2f} kg to reach the perfect BMI of {24.9}.")

    elif weight_diff < 0:
        print(f"{a} You need to lose {abs(weight_diff):.2f} kg to reach the perfect BMI of {24.9}.")
    else:
        print(f"{a} You are already at the perfect BMI.")

    print(f"{a} Your are obese")