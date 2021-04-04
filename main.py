# My Surveying Calculater
import math
import cmath


modes = ('-> Distance calculation', '-> Join calculation')

# Set orgin values
Dis = 0  # Distance value


# Function
# Distance function
def Dis_cal(dN, dE):
    Dis = math.sqrt(dN * dN + dE * dE)
    return Dis


# Introduction
print("Welcome to my Calculater")
print()
print()
# Show which funtions are support
print("Support function modes")
for items in modes:
  print(items)
print()

# Choose function.
while True:
    mode = input("Which function you need: ")
    print()
    print()

    if mode == '1':
        # Distance calculation
        print("Distance calcultion \n")
        # input ΔN and ΔE
        delta_N = float(input("Please input the ΔN: "))
        delta_E = float(input("Please input the ΔE: "))
        print()
        # Result
        print("The distance between two coordinate is {}m. ".format(
            Dis_cal(delta_N, delta_E)))
        print()
        print()

    # Stope the calculater
    elif mode == 'e' or 'E':
        break
        print("See you ~")

    else:
        print("Error !! Please try again.")



# Notes for amount
# int() is interger
# float() can input decimals
# math.floor(n) will return the closest integer value
# math.trunc(n) cut d.p. just keep integer number
# '//' Rounds down to nearest integer
# math.sqrt() to find the square root of any positive real number (integer or decimal)
# isqrt() returns the integer square root of a non-negative integer.

# Degree and radians Translate:
# math.radians() convert degrees to radians
# math.degrees() convert radians to degrees

# Trigonometric Values:
# math.sin(), math.cos(), math.tan()
# math.asin(), math.acos(), math.atan()
# math.hypot() hypotenuse of a triangle


# Problem need to be fixed
  # 存儲變量
    # 每次重啓？
    # 儲存變量 N,E
    # 會否在使用下一個function時，產生混亂
      # need detact