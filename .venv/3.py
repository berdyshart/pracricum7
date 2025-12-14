num = int(input("Enter number"))
flaq = str((num**0.5)) == str(int((num**0.5)))+".0"
while not(flaq):
    num = int(input("Enter number"))
    flaq = str((num ** 0.5)) == str(int((num ** 0.5))) + ".0"