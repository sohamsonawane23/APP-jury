print("soham sonawane")


def temperature_converter(direction):
    # Closure captures the direction internally

    def c_to_f(celsius):
        return (celsius * 9 / 5) + 32

    def f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    if direction == "CtoF":
        return c_to_f
    elif direction == "FtoC":
        return f_to_c
    else:
        raise ValueError("Invalid direction. Use 'CtoF' or 'FtoC'.")


# Create closures for each conversion
celsius_to_fahrenheit = temperature_converter("CtoF")
fahrenheit_to_celsius = temperature_converter("FtoC")

# Usage examples
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f:.2f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F is {temp_c:.2f}°C")
