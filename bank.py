customer={}
pins={}
def create(cus_name):#this module creates account
    new_pin=input("Set a 4 digit PIN: ")
    while not new_pin.isdigit() or len(new_pin)!=4:
        print("PIN must be exactly 4 digits")
        new_pin=input("Set a 4 digit PIN: ")
    customer[cus_name]=0
    pins[cus_name]=new_pin
    print("Account created for",cus_name,"with balance 0")
def balance(cus_name):#this module shows balance
    print("Balance for",cus_name,":",customer[cus_name])
def withdraw(cus_name):#this module deducts amount from account
    amount=input("Enter amount to withdraw: ")
    if check_pin(cus_name)==False:
        return
    while amount.replace(".","",1).isdigit()==False or float(amount)<=0:
        print("Please enter a valid amount greater than zero")
        amount=input("Enter amount to withdraw: ")
    amount=float(amount)
    if amount>customer[cus_name]:
        print("Insufficient balance")
    else:
        customer[cus_name]-=amount
        print("Withdrew",amount," New balance:",customer[cus_name])
def deposit(cus_name):#this module add amount to account
    amount=input("Enter amount to be deposited: ")
    if check_pin(cus_name)==False:
        return
    while not amount.isdigit() or int(amount)<=0:
        print("Please enter a valid amount greater than zero")
        amount=input("Enter amount to be deposited: ")
    amount=int(amount)
    customer[cus_name]+=amount
    print("Deposited",amount)
def check_pin(cus_name):#checks if pin is correct
    p=input("Enter your PIN: ")
    if p==pins[cus_name]:
        return True
    print("Incorrect PIN ")
    return False
def menu(cus_name):#input choises from user
    while True:
        print("\n enter 1 to show balance \n enter 2 to deposit amount \n enter 3 to withdraw amount \n enter 4 to exit")
        choice=input("enter the choice:")
        if choice=="1":
            balance(cus_name)
        elif choice=="2":
            deposit(cus_name)
        elif choice=="3":
            withdraw(cus_name)
        elif choice=="4":
            break
        else:
            print("invalid choice")
while True:
    cus_name=input("\n enter customer name: ").lower()
    if cus_name=="admin123":
        p=input("enter password: ")
        if p=="123456":
            break
        print("incorrect password")
        continue
    if cus_name not in customer:
        print("customer not found")
        c=input("enter 1 to create new account, 0 to exit \n enter the choice: ")
        if c=="1":
            create(cus_name)
        elif c!="0":
            print("invalid choice")
        continue
    entered_pin=input("enter your pin: ")
    if pins[cus_name]!=entered_pin:
        print("invalid pin")
        continue
    menu(cus_name)
print("\n")
print("all customers and their balances:")
for name,bal in customer.items():
    print(name,"-",bal)