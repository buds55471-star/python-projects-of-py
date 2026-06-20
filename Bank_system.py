''' 1. Create account 
2. Deposit
3. Withdraw
4. Check balance
5. Exit'''
student = {}

def add_account(name, amount):
    student[name] = amount
    print('Account added sucessfully...')

def deposit(name, new_amount):
    if name in student:
        student[name]+=new_amount
        print('Updated Balance: ', student[name])
    else:
        print('Name was not found!')

def withdraw(name, amount):
    if name in student:
        if student[name] >= amount:
            student[name]-= amount
            print('Withdraw amount successfully')
            print('Remaining amount: ', student[name])
    else:
        print('Insufficient balance')

def check_balance(name, amount):
    for name, amount in student.items():
        print(f"{name}:{amount}")

while True:
    print('---- Bank Management System ----')
    print('1. Create Account')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Check balance')
    print('5. Exit')

    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        name = input("Enter user name: ")
        amount = int(input("Enter amount: "))
        add_account(name, amount)
        
    elif choice == 2:
        name = input("Enter user name who want to deposit: ")
        new_amount = int(input("Enter deposit amount: "))
        deposit(name, new_amount)
        
    elif choice == 3:
        name = input("Enter user name who want to withdraw: ")
        amount = int(input("Enter Withdraw amount: "))
        withdraw(name, amount)
        
    elif choice == 4:
        check_balance(name, amount)

    else:
        print('Good Bye....')
        break
