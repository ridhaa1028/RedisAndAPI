import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

class StockDataVisualizer:
    """
    A class for visualizing stock data.
    """

    @staticmethod
    def visualize_close_price(data, ticker):
        """
        Visualizes the close prices of a stock over time.

        Args:
        - data (dict): The stock data containing the close prices.
        - ticker (str): The stock ticker symbol.

        Returns:
        - None
        """
        dates = list(data["Time Series (Daily)"].keys())
        close_prices = [float(data["Time Series (Daily)"][date]["4. close"]) for date in dates]

        plt.figure(figsize=(14, 7))
        plt.plot(dates, close_prices, marker='o', linestyle='-')
        plt.title(f'{ticker} Close Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.xticks(rotation=45)
        plt.gca().xaxis.set_major_locator(MaxNLocator(50))
        plt.grid(True)
        plt.tight_layout()

        plt.show()
    
    @staticmethod
    def visualize_volume(data, ticker):
        """
        Visualizes the volume traded of a stock over time.

        Args:
        - data (dict): The stock data containing the volume traded.
        - ticker (str): The stock ticker symbol.

        Returns:
        - None
        """
        dates = list(data["Time Series (Daily)"].keys())
        volumes = [float(data["Time Series (Daily)"][date]["5. volume"]) for date in dates]

        plt.figure(figsize=(14, 7))
        plt.plot(dates, volumes, marker='o', linestyle='-')
        plt.title(f'{ticker} Volume Traded Over Time')
        plt.xlabel('Date')
        plt.ylabel('Volume Traded')
        plt.xticks(rotation=45)

        max_volume = max(volumes)
        if max_volume > 1e6:
            formatter = FuncFormatter(lambda x, _: '{:.0f}M'.format(x / 1e6))
        else:
            formatter = FuncFormatter(lambda x, _: '{:.0f}K'.format(x / 1e3))
        plt.gca().yaxis.set_major_formatter(formatter)

        plt.gca().xaxis.set_major_locator(MaxNLocator(20))

        plt.grid(True)
        plt.tight_layout()

        plt.show()


# Example usage
# StockDataVisualizer.visualize_close_price(data)