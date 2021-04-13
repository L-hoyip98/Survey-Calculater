# My Surveying Calculater
import math
import cmath  # Calculation symbol
import numpy  # Data analysis
from tabulate import tabulate  # For create table

modes = ('-> Distance calculation: 1', '-> Join calculation: 2')

# Set orgin values
Dis = 0  # Distance value

# Set a dictionary to store functons menu
Function_menu = {
    'Function': ['Distance Calculation', 'Join calculation', 'Exit'],
    'Command': ['1', '2', '"e" or "E"']
}


### Function
# Distance function
def Dis_cal(dN, dE):
    Dis = math.sqrt(dN * dN + dE * dE)
    return Dis


# Join calculation ---> calculate the direction from A to B
def Direct_cal(dN, dE):
    WCB = math.atan(dE / dN)

    if dN > 0 and dE > 0:
        return float(WCB)
    elif dN < 0 and dE > 0:
        Adj_WCB = WCB + 180
        return float(Adj_WCB)
    elif dN < 0 and dE < 0:
        return float(Adj_WCB)
        Adj_WCB = WCB + 180
    else:
        Adj_WCB = WCB + 360
        return float(Adj_WCB)


# Decimal degree convert to DDMMSS
def DDMMSS_convert(WCB):
    DD = int(WCB)
    # decimal_WCB = Adj_WCB - numpy.fix(Adj_WCB)     # get the Digits after the decimal point
    decimal_WCB = WCB - DD
    MM = decimal_WCB // 60
    decimal_WCB = decimal_WCB % 60
    SS = decimal_WCB
    SS_2dp = float("%0.2f" % SS)

    Final_WCB = print("The direction is: {}-{}-{} (DDMMSS)".format(
        DD, MM, SS_2dp))
    return Final_WCB


### Main programme code

# Introduction
print("Welcome to my Calculater")
print()
print()
# Show which funtions are support
print("Support function modes\n")
print(tabulate(Function_menu, headers='keys'))
print()
# Useless for loop the menu
#for items in modes:
#  print(items)
#print()

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

    elif mode == '2':
        # Join calculation
        print("Join calculation mode \n")
        # input ΔN and ΔE
        delta_N = float(input("Please input the ΔN: "))
        delta_E = float(input("Please input the ΔE: "))
        print()
        # Result
        result = Direct_cal(delta_N, delta_E)
        print("The bearing between A to B: {}".format(float(result)))

    # Stop the calculater
    elif mode == 'e' or 'E':
        break
        print("See you ~")

    else:
        print("Error !! Please try again.")
