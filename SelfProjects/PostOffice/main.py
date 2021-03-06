
accNo=input("Account No : ")
name=input("Name : ")
nomeniName=input("Nomeni Name : ")
address=input("Address : ")
openingDate=input("Opening Date (dd/mm/yyyy) : ")
amount=int(input("Amount : "))

rate=5.8
time=60  #In months
totalAmount=time*amount*(1+(rate*(time/12)))
print(totalAmount)