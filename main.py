from currency_converter import CurrencyConverter

def convert_currency(from_currency, to_currency, amount):
    converter = CurrencyConverter()
    converted_amount = converter.convert(amount, from_currency, to_currency)
    return converted_amount

try:
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the base currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()

    converted_amount = convert_currency(from_currency, to_currency, amount)
    if converted_amount:
        print(f"\n{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
except ValueError:
    print("Please enter a valid numeric amount.")
except Exception as e:
    print(f"An error occurred: {e}")

