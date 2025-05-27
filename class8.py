# Create a class TemperatureConverter with methods to:
# Convert Celsius to Fahrenheit

# Convert Fahrenheit to Celsius

# (Formulas:
# °C to °F → (°C × 9/5) + 32
# °F to °C → (°F − 32) × 5/9)

class TemperatureConverter:
    def Celsius_to_Fahrenheit(self,celsius):
        return (celsius * 9/5) + 32

    def Fahrenheit_to_Celsius(self,fahrenheit):
        return (fahrenheit-32) * 5/9
    
    
converter = TemperatureConverter()

# Celsius to Fahrenheit
print("30°C =", converter.Celsius_to_Fahrenheit(30), "°F")

# Fahrenheit to Celsius
print("86°F =", converter.Fahrenheit_to_Celsius(86), "°C")


    # OR
#no need to create object
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
print(TemperatureConverter.celsius_to_fahrenheit(30))
print(TemperatureConverter.fahrenheit_to_celsius(86))
