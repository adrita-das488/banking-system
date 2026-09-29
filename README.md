# banking-system
Simple Banking System

A command-line banking application written in Python. It lets customers create an account protected by a 4-digit PIN, check their balance, deposit money and withdraw money. An admin login(admin123 , pin-123456) ends the program and displays every customer with their balance. All data is stored in dictionaries.


Features:

1.Create a new account with a 4-digit PIN (the name is stored in lowercase so it is not case sensetive)
2.PIN validation as pin must be exactly 4 digits
3.Login using customer name and PIN
4.Check account balance
5.Deposit money (whole numbers greater than zero, PIN required)
6.Withdraw money (decimals allowed, must be greater than zero, PIN required)
7.Insufficient balance check on withdrawal
8.Input validation for amounts and menu choices
9.Admin login that shuts down the program and prints all customers and their balances


Technologies / Tools Used:

1.Python 3
2.pycharm
3.Built-in data structures (dictionaries) for storing accounts and PINs

Steps to Install and Run:

Make sure Python 3 is installed. Check with:
       python --version
2. Clone the repository:
       git clone https://github.com/<your-username>/<your-repo-name>.git
3. Move into the project folder:
       cd <your-repo-name>
4. Run the program:
       python bank.py


How to Use:

1. Enter a customer name. If it does not exist, choose 1 to create a new account and set a 4-digit PIN.
2. Enter the name again and your PIN to log in.
3. Use the menu:
   - 1 - Show balance
   - 2 - Deposit amount
   - 3 - Withdraw amount
   - 4 - Exit to the login screen
4. To stop the program, log in as admin (name: 'admin123', password: '123456'). The program then prints all customers and their balances.


Instructions for Testing

This project is tested manually. Run the program (python main.py) and follow the steps below.
1. Test account creation
   - Enter a new customer name.
   - Choose 1 to create an account and set the PIN 1234.
   - Expected: "Account created for <name> with balance 0".
2. Test invalid PIN format while creating an account
   - Enter a PIN like 123 or 12a4.
   - Expected: "PIN must be exactly 4 digits" and it asks again.
3. Test login with a wrong PIN
   - Enter an existing name and a wrong PIN.
   - Expected: "invalid pin" and you return to the name prompt.

4. Test login with an unknown customer
   - Enter a name that has not been created.
   - Expected: "customer not found" with the option to create an account.
5. Test show balance
   - Log in and choose 1.
   - Expected: The current balance is displayed (0 for a new account).
6. Test deposit
   - Choose 2, enter 500 and the correct PIN.
   - Expected: "Deposited 500". Check the balance to confirm it is 500.
7. Test deposit with invalid amounts
   - Enter -5, 0 or abc as the amount, then the correct PIN.
   - Expected: "Please enter a valid amount greater than zero" and it asks again.
8. Test withdrawal
   - Choose 3, enter 200 and the correct PIN.
   - Expected: "Withdrew 200.0 New balance: 300.0".
9. Test withdrawal with insufficient balance
   - Enter an amount larger than the balance.
   - Expected: "Insufficient balance" and the balance stays unchanged.
10. Test wrong PIN during a transaction
    - Choose deposit or withdraw and enter a wrong PIN.
    - Expected: "Incorrect PIN" and the transaction is cancelled.
11. Test invalid menu choice
    - Enter 9 or any value other than 1 to 4.
    - Expected: "invalid choice" and the menu is shown again.
12. Test exit from the menu
    - Choose 4.
    - Expected: You return to the customer name prompt.
13. Test admin login with a wrong password
    - Enter admin123 and a wrong password.
    - Expected: "incorrect password" and you return to the name prompt.
14. Test admin login and program shutdown
    - Enter admin123 and the password 123456.
    - Expected: The program ends and prints all customers with their balances.
