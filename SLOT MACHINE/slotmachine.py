import random

MAX_LINES = 3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3
symbol_count={
    "A": 3,
    "B": 6, 
    "C": 8,
    "D": 10
}
symbol_value={
    "A": 10,
    "B": 6,
    "C": 4,
    "D": 3
}
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        full_match = True  

        
        for column in columns:
            if column[line] != symbol:
                full_match = False
                break
        if full_match:          
                winnings += values[symbol] * bet
                winning_lines.append(f"Line {line+1}-(Full Match)")
        elif columns[0][line] == columns[1][line] or columns[1][line] == columns[2][line]:
                winnings += values[symbol] * (bet // 4)  
                winning_lines.append(f"Line {line+1}-(Partial Match)")

    return winnings , winning_lines 




def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column=[]
        current_symbols= all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value) 
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):   
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns) -1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
        print()
def deposit():
    while True:
        amount=input("What would you like to deposit $: ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please Enter a valid number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid numbers of lines.")
        else:
            print("Please Enter a valid number")
    return lines
def get_bet():
    while True:
        amount=input("What would you like to bet on each line? $: ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} & $ {MAX_BET}.")
        else:
            print("Please Enter a valid number")
    return amount

def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
                print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break        
   
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: $ {total_bet}")
    balance-=total_bet
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine((slots))
    winnings, winning_lines= check_winnings(slots,lines,bet,symbol_value)
    if winnings > 0:
        print(f"Congratulations! You won ${winnings}.")
        print(f"You won on line :", *winning_lines)
    else:
        print("No winnings this time. Better luck next spin!")
    balance += winnings  
    print(f"New balance: ${balance}\n")  
    if balance==0:
        print("You have lost all your money.Game over!")
        return 0
    return balance          

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance} ")
        answer=input("Press Enter to play (q to quit)")
        if answer.lower()=="q":
            break
        balance=spin(balance)
        if balance==0:
            break
    print(f"You left with $ {balance} Thanks for playing!")
main()