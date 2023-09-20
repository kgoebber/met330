########################################################################
# Temperature Conversion Program
#
# By: Kevin Goebbert
# Date: 16 September 2017
#
########################################################################


def tmpf2tmpc():
    '''Write a conversion program to go from temperature in Fahrenheit to Celsius'''


def tmpc2tmpf():
    '''Write a conversion program to go from temperature in Celsius to Fahrenheit'''


def tmpc2tmpk():
    '''Write a conversion program to go from temperature in Celsius to Kelvin'''


def tmpk2tmpc():
    '''Write a conversion program to go from temperature in Kelvin to Celsius'''


# Start of main program

# Get input from standard input, the temperature and unit must be separated by a space
temp, temp_unit = input("Enter a temperature with unit (e.g., 45 F): ").split()
out_unit = input("Enter the desired temperature unit (C, F, or K): ")

# Output the values read in from standard input to standard output
print(temp, temp_unit)
print()
print(out_unit)
