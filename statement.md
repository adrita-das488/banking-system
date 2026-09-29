# Project Statement

## Problem Statement

Small banks, learners and training environments often need a simple way to understand or demonstrate how basic banking operations work, but full banking software is complex, expensive and hard to set up. Manual record keeping is also slow and error-prone, and it offers no protection against unauthorized access to an account.

This project addresses that gap by providing a lightweight, easy-to-run command-line banking system. It lets customers create accounts, secure them with a PIN, and carry out everyday transactions (checking balance, depositing and withdrawing money) with proper input validation, while giving an administrator a way to view all customer balances.

## Scope of the Project

### In Scope

- Creating customer accounts with a 4-digit PIN
- Customer login using name and PIN
- Checking account balance
- Depositing money into an account
- Withdrawing money from an account with a sufficient-balance check
- PIN verification before every transaction
- Validation of PINs, amounts and menu choices
- Admin login that ends the program and displays all customers with their balances
- Command-line (text-based) interface using Python 3

### Out of Scope

- Permanent data storage (data is kept in memory and is lost when the program closes)
- Graphical or web-based interface
- Transfers between accounts
- Transaction history or account statements
- Encryption or hashing of PINs and admin credentials
- Online or network-based banking
- Interest calculation, loans or other advanced banking services

## Target Users

- Students and beginners learning Python and basic programming concepts
- Teachers and trainers who need a simple demonstration of banking logic
- Developers who want a base project to extend with a database, GUI or extra features
- Small groups or practice environments that need a basic account and transaction simulator
- Administrators (in this project, a single admin) who need to review all customer balances

## High-Level Features

- Account creation: register a new customer with a secure 4-digit PIN
- Secure login: access an account using name and PIN
- Balance inquiry: view the current account balance at any time
- Deposit: add money to an account after PIN verification
- Withdrawal: take money out after PIN verification, with a check that funds are sufficient
- Input validation: rejects invalid PINs, amounts, zero or negative values, and wrong menu choices
- Menu-driven interface: simple numbered options that are easy to follow
- Admin access: password-protected admin login that shuts down the program and lists all customers with balances
