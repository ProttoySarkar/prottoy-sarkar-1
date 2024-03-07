"""
for i in range(11):
    print("Number:",i) 

for i in range(99):
    print("Number",i)
    """
"""
for i in range (1,51,2):
    print("Odd number",i)
    """
"""
for i in range (20,23):
    print("Obtained Score and Grade information of roll",i)
    for j in range (3):
        if j == 0:
            number = int(input("Obtained number in Bangla:"))
            if number >80:
                print("Scored Grade A+")
            else:
                print("Scored below Grade A+")
        elif j == 1:
            number= int(input("Obtained Number in English:"))
            if number >= 80:
                print("Score Grade A+")
            else:
                print("scored below Grade A+ ")    
        else:
            number = int(input("obtained number in Math:"))
            if number >= 80:
                print("Score Grade A+")
            else:
                print("Scored below Grade A+")

"""

while True:
    number1=int(input("Enter the number1:"))
    number2=int(input("Enter the number 1:"))
    if number2==0:
        break
    else:
        result = number1/number2
        print("Result:",result)
        continue