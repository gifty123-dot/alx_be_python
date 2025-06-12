from temp_conversion_tool import convert_to_celsius, convert_to_fahrenheit

def main():
    Temperature = int(input("Enter the temperature to test:"))
    Choice = input("Is it in Celsius or Fahrenheit?")
    if Choice == "Celsius":
        convert_to_fahrenheit(Temperature)
    elif Choice == "Fahrenheit":
        convert_to_celsius(Temperature)
    else:
        print("Please Include a valid choice")

if __name__ == "__main__":
    main()
