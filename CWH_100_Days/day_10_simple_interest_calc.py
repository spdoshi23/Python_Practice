print("THIS IS A DYNAMIC CALCULATOR WHICH CALCULATES AMOUNT OF INTEREST")
P = float(input("Enter your principal amount here:  "))
R = float(input("Enter your interest rate here:  "))
T = float(input("Enter your time in years here:  "))
SI = (P*R*T)/100
print("Amount of simple interest at rate", R, "percentage and principal amount of", P, "for", T, "years is", SI )