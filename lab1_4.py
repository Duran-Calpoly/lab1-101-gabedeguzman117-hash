def calculate_average(num1, num2, num3):
    return (num1+num2+num3)/3

def add_tax(bill_total):
    tax_rate = 0.10
    tax_amount = tax_rate*bill_total
    return bill_total+tax_amount 

def greet_user(name):
    return f"Hello {name}"
