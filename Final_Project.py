import requests
import matplotlib.pyplot as plt
import datetime

# This function was assisted by Microsoft Copilot to optimize performance
# Fetch historical price data for a given cryptocurrency from CoinGecko
def get_historical_prices(crypto):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days=30"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract price values from API response
        prices = [price[1] for price in data["prices"]]

        # Convert timestamps to readable date format
        dates = [datetime.datetime.fromtimestamp(price[0] / 1000).strftime('%Y-%m-%d') for price in data["prices"]]

        return dates, prices
    else:
        print("Error fetching data")
        return [], []

# This function was assisted by Microsoft Copilot to optimize performance
# Generate and display a price trend graph for the selected cryptocurrency
def price_trend(dates, prices, crypto):
    plt.figure(figsize=(10, 5))  # Set figure size
    plt.plot(dates, prices, marker='o', linestyle='-', color='b', label=f"{crypto.capitalize()} Price (Last 30 Days)")

    # Formatting plot details
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{crypto.capitalize()} Price Trend Over Last Month")
    plt.legend()
    plt.grid()

    # Show the plot
    plt.show()


# Prompt user to enter a cryptocurrency name
crypto = input("Enter the cryptocurrency (e.g., bitcoin, ethereum): ").lower()

# Retrieve price data
dates, prices = get_historical_prices(crypto)

# If data retrieval is successful, plot the price trend
if prices:
    price_trend(dates, prices, crypto)
else:
    print("Couldn't retrieve price data.")
