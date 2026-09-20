customers={}
pins={}
# to check pin
def check_pin(cus_name):
    attempts=0
    while attempts<3:
        pin=input("Enter your PIN: ")
        if pin==pins[cus_name]:
            return True
        attempts+=1
        print("Incorrect PIN. Attempts left:",3-attempts)
    print("Too many wrong attempts. Transaction cancelled.")
    return False
#to show balance
def show_balance(cus_name):
    print("Balance for",cus_name,":",customers[cus_name])
#to deposit money
def deposit(cus_name):
    amount=input("Enter amount to be deposited: ")
    if check_pin(cus_name)==False:
        return
    while not amount.isdigit() or int(amount)<=0:
        print("Please enter a valid amount greater than zero.")
        amount=input("Enter amount to be deposited: ")
    amount=int(amount)
    customers[cus_name]+=amount
    print("Deposited",amount,". New balance:",customers[cus_name])
#to withdraw money
def withdraw(cus_name):
    amount=input("Enter amount to be withdrawn: ")
    if check_pin(cus_name)==False:
        return
    while amount.replace(".","",1).isdigit()==False or float(amount)<=0:
        print("Please enter a valid amount greater than zero.")
        amount=input("Enter amount to be withdrawn: ")
    amount=float(amount)
    if amount>customers[cus_name]:
        print("Insufficient balance")
    else:
        customers[cus_name]-=amount
        print("Withdrew",amount,". New balance:",customers[cus_name])
#to create an account and store pin
def create_account(cus_name):
    pin=input("Set a 4 digit PIN: ")
    while not pin.isdigit() or len(pin)!=4:
        print("PIN must be exactly 4 digits.")
        pin=input("Set a 4 digit PIN: ")
    customers[cus_name]=0
    pins[cus_name]=pin
    print("Account created for",cus_name,"with balance 0")
#running the process
while True:
    cus_name=input("\nEnter customer name: ").lower()
    if cus_name=="admin123":
        password=input("Enter password: ")
        if password=="123456":
            break
        else:
            print("Incorrect password")
            continue
    if cus_name not in customers:
        print("Customer not found")
        c=input("Enter 1 to create new account, 0 to exit to name input: ")
        if c=="1":
            create_account(cus_name)
        elif c=="0":
            continue
        else:
            print("Invalid choice")
            continue
    while True:
        print("\n")
        print("Enter 1 to Show Balance")
        print("Enter 2 to Deposit Amount")
        print("Enter 3 to Withdraw Amount")
        print("Enter 4 to Exit")
        c2=input("Enter your choice: ")
        if c2=="1":
            show_balance(cus_name)
        elif c2=="2":
            deposit(cus_name)
        elif c2=="3":
            withdraw(cus_name)
        elif c2=="4":
            break
        else:
            print("Invalid choice")
            continue

print("\n")
print("All customers and their balances:")
for customer_name,balance in customers.items():
    print(customer_name,":",balance)