# Stock Market Data Extraction
Python script to extract stock price time series data from <a href="https://alphavantage.co">Alpha Vantage</a>.

## Prerequisites
- Install the latest version of Python.
- Get an API key from <a href="https://alphavantage.co">Alpha Vantage</a>.
- Copy `.env.example` to `.env` using the following command:

```
mv .env.example .env
```
- Replace the API key in `.env` file with your API key from Alpha Vantage.

## Setup
Run the following commands from root directory to get started:
1. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
2. Install the dependencies
```
pip install req.txt
```
3. Run the script:
```
python exchange.py
```

## Licences
Nil