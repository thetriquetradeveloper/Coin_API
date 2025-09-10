from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import logging
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os
import argparse
import sys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

class coin:
    """
    coin class for fetching cryptocurrency price and market cap information.

    Hints:
    - Use the 'silent' parameter to suppress logs (silent=True by default).
    - The class scrapes CoinMarketCap and Coinbase, so results may change if their page layouts change.
    - Requires a working internet connection.
    - If you get "Network Error", check your network or if CoinMarketCap is blocked.
    - If the output is missing the market cap, the Coinbase page structure may have changed or loaded too slowly.
    - The arrow indicates price movement direction (↗️ for up, ↘️ for down).
    - For troubleshooting, run with silent=False to see more output.
    - Example usage: coin("bitcoin").give_price()
    """

    def __init__(self, link, silent=True):
        """
        Initialize the coin object.

        Hints:
        - 'link' should be the coin's slug as used in CoinMarketCap URLs (e.g., 'bitcoin', 'ethereum').
        - Set 'silent=False' to see Selenium and driver logs for debugging.
        """
        self.link = link
        self.silent = silent
        
        # Disable all logging if silent mode is enabled
        if self.silent:
            logging.getLogger('selenium').setLevel(logging.CRITICAL)
            logging.getLogger('urllib3').setLevel(logging.CRITICAL)
            logging.getLogger('webdriver_manager').setLevel(logging.CRITICAL)
            logging.disable(logging.CRITICAL)
        
        options = Options()
        service = Service(log_path="NUL")
        
        # Comprehensive logging suppression
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-logging-redirect")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-sync")
        options.add_argument("--disable-translate")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-first-run")
        options.add_argument("--no-service-autorun")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-component-extensions-with-background-pages")
        options.add_argument("--disable-ipc-flooding-protection")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-hang-monitor")
        options.add_argument("--disable-prompt-on-repost")
        options.add_argument("--disable-component-update")
        options.add_argument("--disable-features=TranslateUI,Notification,MediaRouter,OptimizationHints")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-domain-reliability")
        options.add_argument("--safebrowsing-disable-auto-update")
        options.add_argument("--safebrowsing-disable-download-protection")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--headless=new")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        options.add_argument("--remote-debugging-port=0")
        
        # Additional silent options
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-oopr-debug-crash-dump")
        options.add_argument("--no-crash-upload")
        options.add_argument("--disable-gpu-sandbox")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-features=VizDisplayCompositor")

        options.set_capability("pageLoadStrategy", "eager")

        # Environment variables for logging suppression
        os.environ["WDM_LOG_LEVEL"] = "0"
        os.environ["CHROME_LOG_FILE"] = os.devnull
        os.environ["PYTHONWARNINGS"] = "ignore"
        os.environ["SELENIUM_LOG_LEVEL"] = "0"

        self.web = web = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        self.web.get(f"https://coinmarketcap.com/currencies/{self.link}/")
        self.wait = WebDriverWait(web, 10)

    def get_text_with_retry(self, driver, by, value, wait, retries=3):
        """
        Helper function to get text from a web element with retries.

        Hints:
        - Retries up to 3 times if the element is stale.
        - Useful for dynamic web pages where elements may reload.
        """
        for _ in range(retries):
            try:
                elem = wait.until(EC.visibility_of_element_located((by, value)))
                return elem.text
            except StaleElementReferenceException:
                time.sleep(0.5)
        raise Exception("Element is persistently stale")

    def give_price(self):
        """
        Fetches the current price, symbol, daily change, and market cap for the given coin.

        Hints:
        - Requires a working internet connection.
        - If you get "Network Error", check your network or if CoinMarketCap is blocked.
        - If the output is missing the market cap, the Coinbase page structure may have changed or loaded too slowly.
        - The arrow indicates price movement direction (↗️ for up, ↘️ for down).
        - The function scrapes CoinMarketCap and Coinbase, so results may change if their page layouts change.
        - For troubleshooting, run with silent=False to see more output.
        - Example: coin("bitcoin").give_price()
        """
        # Hint: This checks if CoinMarketCap is reachable. If not, returns "Network Error".
        try:
            response = requests.get("https://coinmarketcap.com", timeout=10)
            if response.status_code != 200:
                return "Network Error"
        except requests.RequestException:
            return "Network Error"  

        self.web.get(f"https://coinmarketcap.com/currencies/{self.link}/")
        wait = self.wait
        # Hint: The following XPaths may break if CoinMarketCap changes their layout.
        symbol = self.get_text_with_retry(self.web, By.XPATH, '//*[@id="section-coin-overview"]/div[1]/h1/div[1]/span', wait)
        price = self.get_text_with_retry(self.web, By.XPATH, '//*[@id="section-coin-overview"]/div[2]/span', wait)
        span_elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="section-coin-overview"]/div[2]/div/div/p')))
        span = span_elem.text
        arrow_color = span_elem.get_attribute("color")
        arrow_d = "↗️" if arrow_color == "green" else "↘️"
        # Hint: Market cap is fetched from Coinbase, not CoinMarketCap.
        self.web.get(f"https://www.coinbase.com/en-gb/price/{self.link}")
        try:
            cap = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div/div/main/section[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/p')
                )
            )
            cap = cap.text
            return f"{symbol} {price} {arrow_d} {span.replace('(1d)', '').strip()} Market Cap: {cap}"
        except TimeoutException:
            if not self.silent:
                print("Could not find the market cap element. The page structure may have changed or it took too long to load." + " and other data is still available")
                print(f"{symbol} {price} {arrow_d} {span.replace('(1d)', '').strip()}")
            return f"{symbol} {price} {arrow_d} {span.replace('(1d)', '').strip()}"



def main():
    """
    Command-line interface for the coin API.
    Usage: coin-price <coin_name>
    Example: coin-price bitcoin
    """
    parser = argparse.ArgumentParser(
        description="Get cryptocurrency price information",
        prog="coin-price"
    )
    parser.add_argument(
        "coin_name", 
        help="Name of the cryptocurrency (e.g., bitcoin, ethereum, cardano)"
    )
    parser.add_argument(
        "--silent", 
        action="store_true", 
        default=True,
        help="Suppress debug output (default: True)"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Show debug output"
    )
    
    args = parser.parse_args()
    
    # Set silent mode based on arguments
    silent_mode = args.silent and not args.verbose
    
    try:
        # Create coin object and get price
        coin_obj = coin(args.coin_name, silent=silent_mode)
        result = coin_obj.give_price()
        print(result)
    except Exception as e:
        if not silent_mode:
            print(f"Error: {e}")
        else:
            print("Error: Unable to fetch coin data. Please check the coin name and your internet connection.")
        sys.exit(1)

if __name__ == "__main__":
    coin_obj = coin("bitcoin")
    result = coin_obj.give_price()
    print(result)
