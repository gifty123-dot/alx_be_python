def safe_divide(numerator, denominator):
    try:
        numerator_number = float(numerator)
        denominator_number = float(denominator)
        result = numerator_number / demoninator_number 
        return f"The result is:{result}"
    except ValueError:
        return "Error: Please provide valid numbers."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

