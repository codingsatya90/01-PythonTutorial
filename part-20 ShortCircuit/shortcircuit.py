# Logical AND: True if both the operands are true x and y
# Logical OR: True if eitherof  the operands is true x and y
# Logical NOT: True if  operand is false not x


# AND operator

ssc = int(input("Enter SSC Number"))
hsc = int(input("Enter HSC Number"))
test = int(input("Enter TEST Number"))
if ssc >= 60 and hsc >= 65 and test >= 76:
    print("Eligible")
else:
    print("Not Eligible")
