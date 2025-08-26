def safe_divide(numerator, denominator):
    try:
        numerator_number = float(numerator)
        denominator_number = float(denominator)
        result = numerator_number / denominator_number 
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

