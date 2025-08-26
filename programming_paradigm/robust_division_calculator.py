def safe_divide(numerator_string, denominator_string):
    try:
        numerator = float(numerator_string)
        denominator = float(denominator_string)
        result = numerator / demoninator 
        return f"The result is:{result}"
    except ValueError:
        return "Error: Please provide valid numbers."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

