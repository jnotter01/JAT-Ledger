from decimal import Decimal


def calculate_summary(transactions):
    total_income = Decimal("0.00")
    total_expenses = Decimal("0.00")

    for transaction in transactions:
        if transaction.transaction_type == "Income":
            total_income += transaction.amount
        elif transaction.transaction_type == "Expense":
            total_expenses += transaction.amount

    net_profit = total_income - total_expenses

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_profit": net_profit,
    }