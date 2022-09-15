import sys
try:
    Fahrenheit = float(sys.argv[1])
except:
    print("the temperature is missing")
    sys.exit(1)
Celsius = (5*(Fahrenheit - 32))/9
print("Temperature in celsius = ", Celsius)