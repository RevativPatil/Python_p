pin = 1234
cb = 2500
for i in range(3):
    p=int(input("Enter your pin:\n"))
    if(pin == p):
        wb=int(input("Enter the Amount you want to widraw:"))
        if(cb>wb):
            cb=cb-wb
            print("Transaction Successful")
            print(cb,"is")
            break
        else:
            print("Insufficient Balance")
    else:
        print("Incorrect pin")
    
     