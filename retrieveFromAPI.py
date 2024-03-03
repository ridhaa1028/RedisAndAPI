import requests
from api_config import get_api_key

class RetrieveFromAPI:
    """
    Class for retrieving daily time series data for a given symbol from the Alpha Vantage API.
    """

    @staticmethod
    def get_daily_time_series(symbol, outputsize='compact'):
        """
        Retrieve daily time series data for a given symbol from the Alpha Vantage API.

        Args:
        - symbol (str): The symbol of the stock or equity.
        - outputsize (str, optional): The size of the output. Default is 'compact' which returns
          last 100 days worth of data. Full will return for past 20 years

        Returns:
        - dict: The JSON response containing the daily time series data.
        """
        base_url = 'https://www.alphavantage.co/query'
        api_key = get_api_key()  # Call the function to get the API key
        url = f'{base_url}?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize={outputsize}&datatype=json&apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            return None

# Example usage
# data = RetrieveFromAPI.get_daily_time_series('RKT')


    