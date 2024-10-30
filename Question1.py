#task1
def weather_forcast():
    while True:
        try:
            temp_farenheit = float(input("Enter the current temperature in Farenheit here:  "))
        except:
            pass
weather_forcast()

#task2

def weather_forcast():
    while True:
        try:
            temp_fahrenheit = float(input("Enter the current temperature in Farenheit here:  "))
            temp_celsius = (temp_fahrenheit - 32) * 5/9
        except ValueError:
            print("Please enter a valid number.")
        else:
            print(f"The temperature in Celsius is {temp_celsius}")
            return temp_celsius
            
weather_forcast()

#task3

def weather_forcast():
    while True:
        try:
            temp_fahrenheit = float(input("Enter the current temperature in Farenheit here:  "))
            temp_celsius = (temp_fahrenheit - 32) * 5/9
        except ValueError:
            print("Please enter a number.")
        else:
            print(f"The temperature {temp_fahrenheit} degrees Farenheit is {temp_celsius} Celsius")
            return temp_celsius
            
weather_forcast()

#task4

def weather_forcast():
    while True:
        try:
            temp_fahrenheit = float(input("Enter the current temperature in Farenheit here:  "))
            temp_celsius = (temp_fahrenheit - 32) * 5/9
        except ValueError:
            print("Please enter a number.")
        else:
            print(f"The temperature {temp_fahrenheit} degrees Farenheit is {temp_celsius} Celsius")
            return temp_celsius
        finally:
            print("Thank you for using the calculator!")
            
weather_forcast()