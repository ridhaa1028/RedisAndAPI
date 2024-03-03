from retrieveFromAPI import RetrieveFromAPI
from retrieveFromRedis import RetrieveFromRedis
from visualization import StockDataVisualizer
from insertToRedis import InsertToRedis
from calculations import Calculations


def main():
    print('Welcome to the Stock Data Retrieval App! It shows you data on the last 100 business days for a ticker.')
    ticker = input('Enter stock ticker: ')
    data = RetrieveFromAPI.get_daily_time_series(ticker)
    InsertToRedis.insertJsonToRedis(ticker, data)

    while True:
        print('Choose an action:')
        print('1. Retrieve and print from Redis')
        print('2. Visualization of closing prices')
        print('3. Visualization of volume')
        print('4. Show me some calculations on the stock data')
        print('5. Show me highest close price')
        print('6. Show me lowest close price')
        print('0. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            output = RetrieveFromRedis.retrieve_all_redis_data(ticker)
            if (output):
                print(output)
            else:
                print('Nothing in Redis')
        
        elif choice == '2':
            StockDataVisualizer.visualize_close_price(data, ticker)
        
        elif choice == '3':
            StockDataVisualizer.visualize_volume(data, ticker)
        
        elif choice == '4':
            stats = Calculations.calculate_statistics(data)
            print('\nStatistics:')
            print(f'Average Volume: {stats[0]} shares')
            print(f'Average Close Price: ${stats[1]}')
            print(f'Change in Price: ${stats[2]}')
            
        elif choice == '5':
            high = Calculations.calculate_highest_closing_price(data)
            print(f'Highest CLosing Price: {high}')
            
        elif choice == '6':
            low = Calculations.calculate_highest_closing_price(data)
            print(f'Highest CLosing Price: {low}')
        
        elif choice == '0':
            break

        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()

    
    
