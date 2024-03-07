"""
#An example on logical operator
a=15
b=8

print(a<b and b>a)           #and
print(a>b and b<a)           #or
print(not(a>b and b<a))      #not

# question no 1 
print("enter a number")
a=input()
a=int(a)

if a%2==0:
    print("a is even ")
else:
    print("a is odd")    

#Question no 2 
x=input("rectrangle length")
y=input(" rectrangle width")
area=int(x)*int(y)
print(area)
"""
# Question no 3
print(" enter score")
a=input()
a=int(a)
print(" enter perchantage")
b=input()
b=int(b)

if (a>=33 and b<=75):
    print("passed")
else:
    print("failed")    