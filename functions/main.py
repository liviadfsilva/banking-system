import textwrap

def menu():
    menu = """
    Choose an option below.

    [1] Deposit
    [2] Withdraw
    [3] Statement
    [4] Quit
    \n"""
    
    return int(input(textwrap.dedent(menu)))

def deposit(balance, amount, statement):
    if amount <= 0:
        print("You can only deposit amounts greater than or equal to $1")
    else:
        balance += amount
        statement += f"Deposit: ${amount:.2f}\n"
        print("The transaction was successful. Thank you!")
        return balance, statement

def withdraw(balance, amount, statement, withdrawal_limit, limit, nr_withdrawals):
    if nr_withdrawals == withdrawal_limit:
        print("Sorry. You can only make a withdrawal up to 3x a day. Please try again tomorrow.")
    elif balance == 0:
        print("You must have a balance to make a withdrawal.")
    else:
        if amount > limit:
            print(f"You can only withdrawl up to ${limit} a time.")
        elif amount > balance:
            print("You don't have enough balance. Please try again.")
        else:
            nr_withdrawals += 1
            new_balance = balance - amount
            balance = new_balance
            statement += f"Withdrawal: ${amount:.2f}\n"
            print(f"The transaction was successful. Thank you!\nHere's your money: ${amount:.2f}")
            
    return balance, statement, nr_withdrawals
        
def show_statement(statement, balance):
    print("================ BANK STATEMENT ================\n")
    print("No transactions were made.\n" if not statement else statement)
    print(f"Balance: ${balance:.2f}\n")
    print("==========================================")

def main():
    balance = 0
    limit = 500
    statement = ""
    withdrawals = 0
    WITHDRAWALS_LIMIT = 3
    
    while True:
        
        option = menu()
        
        if option == 1:
            amount = float(input("How much would you like to deposit?\n$"))
            balance, statement = deposit(balance=balance, amount=amount, statement=statement)
            
        elif option == 2:
            amount = float(input("How much would you like to withdrawl?\n$"))
            balance, statement, withdrawals = withdraw(balance=balance, amount=amount, statement=statement, withdrawal_limit=WITHDRAWALS_LIMIT, limit=limit, nr_withdrawals=withdrawals)
            
        elif option == 3:
            show_statement(statement=statement, balance=balance)
            
        elif option == 4:
            break
        
        else:
            print("You must choose a valid option.")
            
main()
        
        