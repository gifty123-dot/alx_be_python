FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} is {celsius}")
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius} is {fahrenheit}")
    return fahrenheit

def main():
    Temperature = int(input("Enter the temperature to convert:"))
    Choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if Choice == "Celsius":
        convert_to_fahrenheit(Temperature)
    elif Choice == "Fahrenheit":
        convert_to_celsius(Temperature)
    else:
        print("Please Include a valid choice")

if __name__ == "__main__":
    main()
