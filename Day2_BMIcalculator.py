# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI_value = round(weight/ height ** 2)
if BMI_value < 18.5:
   print (f"Your bmi is {BMI_value}, you are underweight.")
elif BMI_value < 25:
     print(f"Your bmi is {BMI_value}, You have a normal weight")
elif BMI_value < 30:
     print(f"Your bmi is {BMI_value}, You are slightly overweight")
elif BMI_value < 35:
       print(f"Your bmi is {BMI_value}, You are obese")
else:
        print("You are clinically obese")




