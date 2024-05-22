# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

# Function to get user input and convert temperature
def convert_temperature():
    # Prompt user to input temperature value
    temperature = float(input("Enter the temperature value: "))
    # Prompt user to input original unit of measurement and convert to lowercase
    original_unit = input("Enter the original unit of measurement (Celsius, Fahrenheit, Kelvin): ").lower()

    # Check the original unit of measurement and perform appropriate conversions
    if original_unit == 'celsius':
        # Convert Celsius to Fahrenheit and Kelvin
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        # Print the converted values
        print(f"{temperature}° Celsius is equal to {fahrenheit}° Fahrenheit and {kelvin} Kelvin.")
    elif original_unit == 'fahrenheit':
        # Convert Fahrenheit to Celsius and Kelvin
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        # Print the converted values
        print(f"{temperature}° Fahrenheit is equal to {celsius}° Celsius and {kelvin} Kelvin.")
    elif original_unit == 'kelvin':
        # Convert Kelvin to Celsius and Fahrenheit
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        # Print the converted values
        print(f"{temperature} Kelvin is equal to {celsius}° Celsius and {fahrenheit}° Fahrenheit.")
    else:
        # Inform user of invalid unit of measurement
        print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")

# Call the function to start the program
convert_temperature()

