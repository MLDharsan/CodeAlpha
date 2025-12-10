import csv
from datetime import datetime

# Hardcoded stock
STOCK_PRICES = {
    "AAPL": 180.50,  # Apple
    "TSLA": 250.75,  # Tesla
    "GOOGL": 140.30,  # Google
    "MSFT": 375.20,  # Microsoft
    "AMZN": 145.80,  # Amazon
    "META": 330.50,  # Meta (Facebook)
    "NVDA": 495.30,  # NVIDIA
    "NFLX": 450.25,  # Netflix
}


def display_available_stocks():
    """Display  stocks"""
    print("\n" + "=" * 60)
    print(" AVAILABLE STOCKS")
    print("=" * 60)
    print(f"{'Stock Symbol':<15} {'Company':<20} {'Price ($)':<15}")
    print("-" * 60)

    stock_names = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.",
        "GOOGL": "Google",
        "MSFT": "Microsoft",
        "AMZN": "Amazon",
        "META": "Meta Platforms",
        "NVDA": "NVIDIA",
        "NFLX": "Netflix"
    }

    for symbol, price in STOCK_PRICES.items():
        company = stock_names.get(symbol, "N/A")
        print(f"{symbol:<15} {company:<20} ${price:<14.2f}")
    print("=" * 60)


def add_stock(portfolio):
    """Add a stock to the portfolio"""
    display_available_stocks()

    while True:
        stock_symbol = input("\n Enter stock symbol (or 'done' to finish): ").upper().strip()

        if stock_symbol == 'DONE':
            break

        if stock_symbol not in STOCK_PRICES:
            print(f"❌ '{stock_symbol}' is not available. Please choose from the list above.")
            continue

        try:
            quantity = int(input(f" Enter quantity for {stock_symbol}: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0!")
                continue

            # Add to portfolio or update existing
            if stock_symbol in portfolio:
                portfolio[stock_symbol] += quantity
                print(f"✅ Updated {stock_symbol}: Total quantity = {portfolio[stock_symbol]}")
            else:
                portfolio[stock_symbol] = quantity
                print(f"✅ Added {quantity} shares of {stock_symbol}")

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    return portfolio


def calculate_portfolio_value(portfolio):
    """Calculate total investment value"""
    total_value = 0
    stock_details = []

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        investment = price * quantity
        total_value += investment

        stock_details.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'investment': investment
        })

    return total_value, stock_details


def display_portfolio(portfolio):
    """Display portfolio summary"""
    if not portfolio:
        print("\n  Your portfolio is empty!")
        return

    total_value, stock_details = calculate_portfolio_value(portfolio)

    print("\n" + "=" * 80)
    print("💼 YOUR PORTFOLIO SUMMARY")
    print("=" * 80)
    print(f"{'Stock':<12} {'Quantity':<12} {'Price ($)':<15} {'Total Value ($)':<20}")
    print("-" * 80)

    for stock in stock_details:
        print(f"{stock['symbol']:<12} {stock['quantity']:<12} "
              f"${stock['price']:<14.2f} ${stock['investment']:<19.2f}")

    print("-" * 80)
    print(f"{'TOTAL INVESTMENT VALUE:':<42} ${total_value:>36.2f}")
    print("=" * 80)


def save_to_txt(portfolio):
    """Save portfolio to a text file"""
    if not portfolio:
        print(" Cannot save empty portfolio!")
        return

    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    total_value, stock_details = calculate_portfolio_value(portfolio)

    try:
        with open(filename, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("STOCK PORTFOLIO TRACKER - SUMMARY REPORT\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")

            f.write(f"{'Stock':<12} {'Quantity':<12} {'Price ($)':<15} {'Total Value ($)':<20}\n")
            f.write("-" * 80 + "\n")

            for stock in stock_details:
                f.write(f"{stock['symbol']:<12} {stock['quantity']:<12} "
                        f"${stock['price']:<14.2f} ${stock['investment']:<19.2f}\n")

            f.write("-" * 80 + "\n")
            f.write(f"{'TOTAL INVESTMENT VALUE:':<42} ${total_value:>36.2f}\n")
            f.write("=" * 80 + "\n")

        print(f"\n✅ Portfolio saved to '{filename}' successfully!")

    except Exception as e:
        print(f"\n❌ Error saving file: {e}")


def save_to_csv(portfolio):
    """Save portfolio to a CSV file"""
    if not portfolio:
        print("❌ Cannot save empty portfolio!")
        return

    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    total_value, stock_details = calculate_portfolio_value(portfolio)

    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            # Write header
            writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share ($)', 'Total Value ($)'])

            # Write data
            for stock in stock_details:
                writer.writerow([
                    stock['symbol'],
                    stock['quantity'],
                    f"{stock['price']:.2f}",
                    f"{stock['investment']:.2f}"
                ])

            # Write total
            writer.writerow([])
            writer.writerow(['TOTAL INVESTMENT', '', '', f"{total_value:.2f}"])

        print(f"\n✅ Portfolio saved to '{filename}' successfully!")

    except Exception as e:
        print(f"\n❌ Error saving file: {e}")


def main_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print(" STOCK PORTFOLIO TRACKER")
    print("=" * 60)
    print("1. Add Stocks to Portfolio")
    print("2. View Portfolio")
    print("3. Save Portfolio to TXT file")
    print("4. Save Portfolio to CSV file")
    print("5. Clear Portfolio")
    print("6. Exit")
    print("=" * 60)


def main():
    """Main function"""
    portfolio = {}

    print("\n" + "=" * 60)
    print(" WELCOME TO STOCK PORTFOLIO TRACKER! ")
    print("=" * 60)
    print("Track your stock investments with ease!")

    while True:
        main_menu()
        choice = input("\n Enter your choice (1-6): ").strip()

        if choice == '1':
            portfolio = add_stock(portfolio)

        elif choice == '2':
            display_portfolio(portfolio)

        elif choice == '3':
            save_to_txt(portfolio)

        elif choice == '4':
            save_to_csv(portfolio)

        elif choice == '5':
            confirm = input("\n  Are you sure you want to clear the portfolio? (yes/no): ").lower()
            if confirm in ['yes', 'y']:
                portfolio.clear()
                print(" Portfolio cleared successfully!")
            else:
                print("❌ Clear operation cancelled.")

        elif choice == '6':
            if portfolio:
                save_option = input("\n Do you want to save before exiting? (yes/no): ").lower()
                if save_option in ['yes', 'y']:
                    file_type = input("Save as TXT or CSV? (txt/csv): ").lower()
                    if file_type == 'txt':
                        save_to_txt(portfolio)
                    elif file_type == 'csv':
                        save_to_csv(portfolio)

            print("\n Thank you for using Stock Portfolio Tracker! Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1-6.")


if __name__ == "__main__":
    main()