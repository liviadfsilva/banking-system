menu ="""
Choose an option below.

[D] Deposit
[W] Withdraw
[S] Statement
[Q] Quit

=> """

balance = 0
limit = 500
statement = ""
withdrawals = 0
WITHDRAWALS_LIMIT = 3

while True:
    option = input(menu).upper()

    if len(option) != 1 or not option.isalpha:
        print("You must choose an option.")
    else:
        if option == "D":
            amount = float(input("How much would you like to deposit?\n$"))
            
            if amount <= 0:
                print("You can only deposit amounts greater than or equal to $1")
            else:
                balance += amount
                statement += f"Deposit: ${amount:.2f}\n"
                print("The transaction was successful. Thank you!")
        
        elif option =="W":
            if withdrawals == WITHDRAWALS_LIMIT:
                print("Sorry. You can only make a withdrawal up to 3x a day. Please try again tomorrow.")
            elif balance == 0:
                print("You must have a balance to make a withdrawal.")
            else:
                amount = float(input("How much would you like to withdrawl?\n$"))
                
                if amount > limit:
                    print(f"You can only withdrawl up to ${limit} a time.")
                elif amount > balance:
                    print("You don't have enough balance. Please try again.")
                else:
                    withdrawals += 1
                    new_balance = balance - amount
                    balance = new_balance
                    statement += f"Withdrawal: ${amount:.2f}\n"
                    print(f"The transaction was successful. Thank you!\nHere's your money: ${amount:.2f}")
                
        elif option == "S":
            print("================ BANK STATEMENT ================\n")
            print("Não foram realizadas movimentações.\n" if not statement else statement)
            print(f"Balance: ${balance:.2f}\n")
            print("==========================================")
            
        elif option == "Q":
            break
        else:
            print("Invalid option.")