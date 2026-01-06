from modals.bank import BankAccount
from modals.expenses import expense, CardExpense, CashExpense
from modals.user import User
from modals.database import create_table
from modals.database import clear_transactions
from datetime import datetime
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")
def main():
    print("EXPENSE TRACKER\n")
    create_table()
    account = BankAccount("Tom", "DE5089787998678700", 2004)
    u = User("Tom" ,account)
    u.load_expenses()
    
    expenses=[
        CardExpense(300, "Food", current_date, current_time),
        CashExpense(200, "Travel", current_date, current_time)
    ]
    print("Processing payments ")
    for exp in expenses:
        if not u.new_expense(exp):
            print("Stop further expenses")
            break
        print(exp.process_payment())
        u.save_expense_to_db(exp)
        
    print("\nExpenses:")
    for exp in u.session_expenses:
        print(exp)
    print("\ntotal expense:", u.total_expense())
    
   
    u.save_expenses()
    print("\nTRANSACTION HISTORY")
    print("-"* 50)
    for t in u.get_transaction_history():
        print(f"{t[0]} {t[1]} | {t[2]} ${t[3]} | {t[4]}")
    print("\nTransaction completed")
if __name__ == "__main__":
    main()
            