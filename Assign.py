#BANK TRANSFER AND AIRTIME RECHARGE
# from Acopening.py import account_opening

from Accopen import account_opening,transfer,Internet,bills,Airtime



print("WELCOME TO JAIZ BANK")
print ("1. Account Opening \n2. Transfer \n3. Internet \n4. Bill and Utility \n5. Airtime")
serv = str(input(": "))
if serv == "1" or serv == "Account Opening":
    account_opening()

elif serv == "2" or serv == "Transfer": 
    transfer()
    print("INVALID REQUEST!")

# INTERNET
elif serv == "3" or serv == "Internet":
    
    Internet()
# BILLS AND UTILITY
elif serv == "4":
    bills()
# AIRTIME
elif serv == "5" or serv == "Airtime":
    
    Airtime()
else:
    print("Invalid Resquest!")

