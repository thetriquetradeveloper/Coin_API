# My Python App

## Overview
This project is a Python application that retrieves cryptocurrency price information from CoinMarketCap and Coinbase using web scraping techniques. It defines a class `coin` that interacts with these websites to fetch the latest price, market cap, and other relevant data for a specified cryptocurrency.

## Installation

To get started with this project, you need to install the required dependencies. You can do this by running the following command in your terminal:

```
pip install -r requirements.txt
```

## Usage

1. Import the `coin` class from the `src` module.
2. Create an instance of the `coin` class by passing the cryptocurrency name (e.g., "bitcoin").
3. Call the `give_price` method to retrieve the current price and market cap information.

### Example

```python
from src.coin_api import coin

coin_instance = coin("bitcoin")
print(coin_instance.give_price())
```

## Dependencies

This project requires the following Python packages:

- `selenium`: For web scraping and browser automation.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
