import os
import requests

API_KEY = os.getenv("API_KEY")  # replace API key in env

if __name__ == "__main__":
    stock = input("Enter stock symbol: ")
    url = f"https://alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={API_KEY}"
    res = requests.get(url).json()
    new_res = res["Time Series (Daily)"]
    for i, key in enumerate(new_res):
        print(i+1)
        print("Date:", key)
        print("Open price:", new_res[key]["1. open"])
        print("Close price:", new_res[key]["4. close"])
        print()