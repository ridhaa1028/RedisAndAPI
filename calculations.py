from datetime import datetime, timedelta

class Calculations:
    
    @staticmethod
    def calculate_statistics(data):
        """
        Calculate statistics for stock data.

        Args:
        - data (dict): The stock data containing daily time series information.

        Returns:
        - tuple: A tuple containing average volume, average close price, and change in price.
        """
        dates = list(data["Time Series (Daily)"].keys())
        close_prices = [float(data["Time Series (Daily)"][date]["4. close"]) for date in dates]
        volumes = [float(data["Time Series (Daily)"][date]["5. volume"]) for date in dates]

        last_100_dates = dates[:100]
        last_100_close_prices = close_prices[:100]

        average_volume = sum(volumes) / len(volumes)
        average_close_price = sum(last_100_close_prices) / len(last_100_close_prices)
        change_in_price = last_100_close_prices[-1] - last_100_close_prices[0]

        return average_volume, average_close_price, change_in_price
    
    @staticmethod
    def calculate_highest_closing_price(data):
        """
        Calculate the highest closing price of a stock.

        Args:
        - data (dict): The stock data containing the close prices.

        Returns:
        - float: The highest closing price.
        """
        dates = list(data["Time Series (Daily)"].keys())
        close_prices = [float(data["Time Series (Daily)"][date]["4. close"]) for date in dates]

        if not close_prices:
            return None

        highest_close_price = max(close_prices)
        return highest_close_price

    @staticmethod
    def calculate_lowest_closing_price(data):
        """
        Calculate the lowest closing price of a stock.

        Args:
        - data (dict): The stock data containing the close prices.

        Returns:
        - float: The lowest closing price.
        """
        dates = list(data["Time Series (Daily)"].keys())
        close_prices = [float(data["Time Series (Daily)"][date]["4. close"]) for date in dates]

        if not close_prices:
            return None

        lowest_close_price = min(close_prices)
        return lowest_close_price

