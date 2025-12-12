class user:
    def __init__(self, candidate_name):
        self.candidate_name = candidate_name
        self.expense = []
    def new_expense(self,expense):
        self.expense.append(expense)
    def total_expense(self):
        return sum(m.expense for m in self.expense)