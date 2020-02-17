import yfinance as yf
import json


class YFinanceDataFetcher:
    def __init__(self, stock_name, period, interval):
        self.stock_history_json = yf.Ticker(stock_name).history(period=period, interval=interval).to_json()

    # Converts targeted json key like "Open" to list of tuples of format (timestamp, index)
    def json_key_to_tuple_list(self, index):
        # parse to dictionary
        dictionary = json.loads(self.stock_history_json)
        # parse to tuple list
        tuple_list = [(k, v) for k, v in dictionary[index].items()]
        return tuple_list

    # UNUSED
    def convert_json_to_tuple_list(self, index_list):
        # parse to dictionary
        dict = json.loads(self.stock_history_json)

        for index in index_list:
            list_key_value = [(k, v) for k, v in dict[index].items()]
            print(index)
            print(list_key_value)