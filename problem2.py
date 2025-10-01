"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # Get temperature value from user
    try:
        temp_value = float(input("Enter temperature value: "))
    except ValueError:
        print("Error: Please enter a valid numeric temperature.")
        return

    # Get unit from user
    unit = input("Enter current unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    # Validate unit input
    if unit not in ['C', 'F']:
        print("Error: Unit must be 'C' or 'F'.")
        return

    # Perform conversion
    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp_value)
        print(f"{temp_value}°C = {converted_temp:.2f}°F")
    else:  # unit == 'F'
        converted_temp = fahrenheit_to_celsius(temp_value)
        print(f"{temp_value}°F = {converted_temp:.2f}°C")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()