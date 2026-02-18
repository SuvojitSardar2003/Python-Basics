# 2. WAP using function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius *(9/5)) + 32
    return fahrenheit

celsius = float(input("Enter temperaure in celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{round(celsius,2)} °C is equal to {round(fahrenheit,2)} °F.")