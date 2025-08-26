def safe_divide(numerator_string, demoninator_string):
    try:
        numerator = float(numerator_string)
        demoninator = float(demoninator_string)
        result = numerator / demoninator 
        return f"The result is:{result}"
    except ValueError:
        return "Error: Please provide valid numbers."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

