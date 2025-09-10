# Coin API

## Overview
A Python package for getting cryptocurrency prices from CoinMarketCap and Coinbase using web scraping techniques. The package provides both a Python API and a command-line interface for retrieving cryptocurrency price information.

## Quick Start

After installation, simply use the command line:

```bash
# Get Bitcoin price
coin-price bitcoin

# Get Ethereum price  
coin-price ethereum

# Get any cryptocurrency price
coin-price <coin_name>
```

That's it! No Python code needed - just type the command and get instant cryptocurrency price information.

**Note**: After installing the wheel, the package name becomes `coin_api` (with underscore) and the command `coin-price` becomes available globally.

## Installation

### Install from Wheel
```bash
# Install dependencies first
pip install -r requirements.txt

# Build the wheel
python -m build

# Install the wheel
pip install dist/coin_api-2.0.0-py3-none-any.whl
```

### Development Installation (for contributors)
```bash
pip install -e .
```

## Usage

### Command Line Interface

After installation, you can use the `coin-price` command:

```bash
# Get Bitcoin price
coin-price bitcoin

# Get Ethereum price with verbose output
coin-price ethereum --verbose

# Get Dogecoin price in silent mode (no logs)
coin-price dogecoin --silent
```

### Python API

After installation, you can also use it as a Python module:

```python
from coin_api import coin

# Create a coin instance
btc = coin("bitcoin")

# Get price information
price_info = btc.give_price()
print(price_info)

# Silent mode (no Selenium logs)
btc_silent = coin("bitcoin", silent=True)
price_info = btc_silent.give_price()
```

### Command Line Arguments

- `coin_name`: Cryptocurrency name (required) - e.g., bitcoin, ethereum, cardano
- `--verbose`: Enable verbose output (disable silent mode)
- `--silent`: Enable silent mode (suppress all logs and output) - default behavior

## Features

- **Command Line Interface**: Simple terminal command - just type `coin-price <coin_name>`
- **Silent Mode**: Completely suppress all Selenium logs and browser output (default)
- **Comprehensive Log Suppression**: Removes all unnecessary browser logging
- **Error Handling**: Graceful handling of network and parsing errors
- **Market Cap Integration**: Fetches data from both CoinMarketCap and Coinbase
- **Easy Usage**: No need to write Python code - just use the command line

## Dependencies

- `selenium>=4.0.0`: For web scraping and browser automation
- `webdriver-manager>=3.8.0`: For automatic Chrome driver management
- `requests>=2.25.0`: For HTTP requests

## Author

**faizan code**  
Email: thetriquetradeveloper@gmail.com  
GitHub: [thetriquetradeveloper](https://github.com/thetriquetradeveloper)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
