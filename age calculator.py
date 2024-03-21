# Python3 code to  calculate age in years
from datetime import date
 
def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age
         
# Driver code
print(calculateAge(date(2008, 10, 9)), "years")