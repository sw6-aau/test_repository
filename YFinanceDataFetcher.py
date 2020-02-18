import yfinance as yf
import json
from MySQLHandler import *


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
    def convert_json_to_tuple_list_and_insert(self, index_list):
        # parse to dictionary
        db_handler = MySQLHandler(host='35.228.117.69', database='stock_data', user='commongroup',
                                  password='Aau123Cas!')
        history_dict = json.loads(self.stock_history_json)

        # PT ret ineffecient at åbne og lukke forbindelsen hver gang men fik en fejl da jeg kun gjorde det en gang, så
        # skal finde en måde at sende flere queries over den samme forbindelse.
        for index in index_list:
            list_key_value = [(k, v) for k, v in history_dict[index].items()]
            sql = "INSERT INTO AMZN_01_02_2020 (timestamp, " + index + ") VALUES (%s, %s) ON DUPLICATE KEY UPDATE " + index + "=VALUES(" + index + ")"
            db_handler.insert(sql, list_key_value)
        db_handler.connection.close()
