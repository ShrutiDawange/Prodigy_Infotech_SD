def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit of measurement (Celsius/C, Fahrenheit/F, Kelvin/K): ").strip().lower()

    if original_unit == 'celsius' or original_unit == 'c':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif original_unit == 'fahrenheit' or original_unit == 'f':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif original_unit == 'kelvin' or original_unit == 'k':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit of measurement. Please enter Celsius/C, Fahrenheit/F, or Kelvin/K.")
        return

    print(f"{temperature} degrees {original_unit.capitalize()} is equal to:")
    print(f"{fahrenheit} degrees Fahrenheit")23
    
    print(f"{kelvin} Kelvin")

if __name__ == "__main__":
    main()
