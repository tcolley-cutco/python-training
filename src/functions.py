

# Optional arguments demo
def some_function(user, first_name, **other_info):
    print(f"User: {user}")
    print(f"First Name: {first_name}")
    print("Last Name: " + other_info.get("last_name"))
    print("Zip: " + other_info.get("zip"))


# Practice Exercise
def tax(rate, *amounts, **tax_brackets):
    taxes = []
    rate = rate / 100
    for amount in amounts:
        taxed_amount = rate * amount
        taxes.append(taxed_amount)

    print(tax_brackets)

    return taxes


def main():
    some_function("tcolley", "Trevor", zip="14760", last_name="Colley")
    amount = [150]
    rate = 5
    tax_brackets = {"US": 8, "CA": 7}
    tax_amount = tax(rate, 150, 200, 250, kwargs_1=tax_brackets)
    print(f"Tax for amount={amount} and rate={rate} is {tax_amount}")


main()
