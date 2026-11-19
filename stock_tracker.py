# Stock Portfolio Tracker
# CodeAlpha Python Programming Internship

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400,
    "GOOGL": 150,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("\n===================================")
print("       STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")

for name, price in stocks.items():
    print(f"{name} : ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you finish.\n")

while True:

    stock_name = input("Enter stock symbol: ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stocks:
        print("Stock not found. Please try again.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

    except ValueError:
        print("Please enter a valid number.\n")
        continue

    price = stocks[stock_name]
    investment = price * quantity

    portfolio.append({
        "name": stock_name,
        "price": price,
        "quantity": quantity,
        "investment": investment
    })

    total_investment += investment

    print("Stock added successfully!\n")


if portfolio:

    print("\n========== PORTFOLIO SUMMARY ==========")

    report = []
    report.append("STOCK PORTFOLIO REPORT")
    report.append("=" * 35)

    for item in portfolio:

        details = (
            f"{item['name']} | "
            f"Price: ${item['price']} | "
            f"Quantity: {item['quantity']} | "
            f"Total: ${item['investment']}"
        )

        print(details)
        report.append(details)

    print("---------------------------------------")
    print("Total Investment: $", total_investment)

    report.append("-" * 35)
    report.append(f"Total Investment: ${total_investment}")

    with open("portfolio_report.txt", "w") as file:
        file.write("\n".join(report))

    print("\nReport saved successfully!")
    print("File: portfolio_report.txt")

else:
    print("\nNo stocks were added to your portfolio.")

print("\nThank you for using Stock Portfolio Tracker!")