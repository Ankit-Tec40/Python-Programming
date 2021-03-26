# Import time module
import datetime
# import relativedlta module for calculation between time and dates
from dateutil.relativedelta import relativedelta
# This function take input for time and handle its exceptions
def inputdate():
    day,month,year=map(int,input("Opening Date (dd/mm/yyyy) : ").split("/"))
    openingdate=datetime.datetime(year,month,day)
    return(openingdate)
# This function Calcute the date after defined months
def calcdate(openingdate):
    openingdatedisplay=openingdate.strftime("%d/%m/%Y")
    closingdate=openingdate+ relativedelta(months=+60)
    closingdatedisplay=closingdate.strftime("%d/%m/%Y")
    print(openingdatedisplay)
    print(closingdatedisplay)
# This Function Calculate the total amount with the interest
def calcamount(amount):
    interest=5.8
    finalamount=amount*interest
    print(finalamount)

# This is the main user class
class users:
    def get(self):
        accNo=input("Account No : ")
        name=input("Name : ")
        nomeniName=input("Nomeni Name : ")
        address=input("Address : ")
        amount=int(input("Amount : "))
        openingdate=inputdate()
        calcdate(openingdate)
        calcamount(amount)

def main():
    ob=users()
    ob.get()

# From here code starts excuting
if __name__=="__main__":
    main()

