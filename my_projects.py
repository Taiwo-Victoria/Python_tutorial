# BUILDING A BMI CALCULATOR

while True:
    try:
        name = input("Kindly register for your name: ")
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        BMI = (weight * 703) / (height  * height )

        if BMI > 0:
            if(BMI < 18.5):
                print(name + " You are underweight, your BMI is: " +str(BMI))
            elif(BMI <= 24.9):
                print(name + " You are normal weight, your BMI is: " +str(BMI))
            elif(BMI <= 29.9):
                 print(name + " You are overweight, kindly excercise more, your BMI is: " + str(BMI))
            elif(BMI <= 34.9):
                print(name + " You are obese, your BMI is: " + str(BMI))
            elif(BMI <= 39.9):
                print(name + " You are severely obese, your BMI is: " + str(BMI))
            else:
                print(name + " You are morbidly obese, your BMI is: " + str(BMI))
                break
        else:
            print(name +" Try again and make sure you provide a positive number!!! ")
            
    except ZeroDivisionError as err:
        print('Not accepting zero (0):', err)
        
    except (RuntimeError, TypeError, NameError, ValueError): 
        print("Oops!  That was no valid number.  Try again...")
        