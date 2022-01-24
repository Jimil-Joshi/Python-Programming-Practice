kg = float(input("Enter KG. of a person: "))
m = float(input("Enter a height of person in meters: "))

def BMI(kg,m):
    bmi = kg/(m*m)
    return bmi 
print(f"BMI for {kg} & {m} is {BMI(kg, m)}")
    