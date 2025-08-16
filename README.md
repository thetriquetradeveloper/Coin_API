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
# My Python App

## Overview
This project is a Python application that retrieves cryptocurrency price information from CoinMarketCap and Coinbase using web scraping techniques. It defines a class `coin` that interacts with these websites to fetch the latest price, market cap, and other relevant data for a specified cryptocurrency.

## Installation

Install the package directly with pip:

```
pip install coin-api==0.1.0
```

(If you previously installed via a requirements file, you can remove that and use the package above.)

## Usage

1. Import the `coin` class from the installed package (adjust import path if the package exposes a different module).
2. Create an instance of the `coin` class by passing the cryptocurrency name (e.g., "bitcoin").
3. Call the `give_price` method to retrieve the current price and market cap information.

### Example

```python
from coin_api import coin

coin_instance = coin("bitcoin")
print(coin_instance.give_price())
```

## Dependencies

This project uses the `coin-api` package (installed via pip as shown above). Remove any prior manual dependency management if you switch to the pip package.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
```

## Dependencies

This project requires the following Python packages:

- `selenium`: For web scraping and browser automation.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
