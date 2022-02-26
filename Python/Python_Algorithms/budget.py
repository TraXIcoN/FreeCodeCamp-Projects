from collections import defaultdict
from itertools import zip_longest


class Category:

    def __init__(self, budget_cat):
        self.budget_cat = budget_cat
        self.balance = 0.
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    
    def check_funds(self, amount):
        return self.balance >= amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.deposit(-amount, description)
        return self.check_funds(amount)
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, other):
        valid_transfer = self.withdraw(amount,
                                       f"Transfer to {other.budget_cat}")
        if valid_transfer:
            other.deposit(amount, f"Transfer from {self.budget_cat}")
        return valid_transfer

    def __repr__(self):
        return f"Category('{self.budget_cat}')"

    def __str__(self):
        head = self.budget_cat.center(30, "*")
        items = []
        for item in self.ledger:
            item_des = item['description'].ljust(23, " ")[:23]
            item_cost = f"{item['amount']:.2f}".rjust(7, " ")[-7:]
            items += [item_des + item_cost]
        total = f"Total: {self.balance:.2f}"
        all_output = [head] + items + [total]
        return ("\n").join(all_output)


def calc_percent_spent(categories):
    amount_spent = defaultdict(int)
    for cat in categories:
        for item in cat.ledger:
            spent = item['amount'] if item['amount'] < 0 else 0
            amount_spent[cat] += abs(spent)
    total_spent = sum(amount_spent.values())
    percent_spent = [amt/total_spent for amt in
                     amount_spent.values()]
    return percent_spent


def create_spend_chart(categories):
    cat_names = [cat.budget_cat for cat in categories]
    percent_spent = calc_percent_spent(categories)
    rows = ["Percentage spent by category"]
    for row in range(100, -1, -10):
        row_title = f"{str(row)}| ".rjust(5, " ")
        values = ["o" if n*100 >= row else " " for n in percent_spent]
        rows += [(row_title + "  ".join(values)).ljust(14, " ")]
    rows += [(" "*4 + "-"*(1+3*len(percent_spent))).ljust(14, " ")]
    rows += [(" "*5 + "  ".join(letters)).ljust(14, " ") for letters in
             zip_longest(*cat_names, fillvalue=" ")]
    return "\n".join(rows)
