import datetime
from dateutil.relativedelta import relativedelta

def dates():
    day,month,year=map(int,input("Opening Date (dd/mm/yyyy) : ").split("/"))
    openingdate=datetime.datetime(year,month,day)
    openingdatedisplay=openingdate.strftime("%d/%m/%Y")
    closingdate=openingdate+ relativedelta(months=+60)
    closingdatedisplay=closingdate.strftime("%d/%m/%Y")
    print(openingdatedisplay)
    print(closingdatedisplay)

def amountcalc(amount):
    interest=5.8
    finalamount=amount*interest
    print(finalamount)




class users:
    def get(self):
        accNo=input("Account No : ")
        name=input("Name : ")
        nomeniName=input("Nomeni Name : ")
        address=input("Address : ")
        amount=int(input("Amount : "))
        dates()
        amountcalc(amount)



def main():
    ob=users()
    ob.get()


if __name__=="__main__":
    main()
