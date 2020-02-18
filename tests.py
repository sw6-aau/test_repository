import unittest
from YFinanceDataFetcher import *
from MySQLHandler import *


class YFinanceDataFetcherTests(unittest.TestCase):
    def setUp(self):
        stock_name = "AMZN"
        period = "2d"
        interval = "1d"
        self.test_stock = YFinanceDataFetcher(stock_name, period, interval)

    # Prints Open, High, Low, Close, Volume, Dividends, Stock Splits
    def test_initialization(self):
        print(self.test_stock.stock_history_json)

    def test_json_key_to_tuple_list(self):
        print(self.test_stock.json_key_to_tuple_list("Open"))

    def test_convert_json_to_tuple_list_and_insert(self):
        index_list = ["Open", "High", "Low", "Close"]

        self.test_stock.convert_json_to_tuple_list_and_insert(index_list)


# For at denne test klasse virkelig giver mening skal vi kunne lave en dummy database
class MySQLHandlerTests(unittest.TestCase):
    def setUp(self):
        self.test_handler = MySQLHandler(host='35.228.117.69', database='stock_data', user='commongroup',
                                         password='Aau123Cas!')

    def tearDown(self):
        self.test_handler.connection.close()

    def test_show_tables(self):
        self.test_handler.show_tables()

    def test_insert(self):
        test_value = [("2")]
        # sql = "INSERT INTO AMZN_01_02_2020 (timestamp) VALUES (%s)"
        list_tuple = [("2", "33")]
        # If the same timestamp / primary key already exist update value2, in this case 'open'
        sql = "INSERT INTO AMZN_01_02_2020 (timestamp, open) VALUES (%s, %s) ON DUPLICATE KEY UPDATE open=VALUES(open)"
        self.test_handler.insert(sql, list_tuple)

    def test_create_table(self):
        sql = "CREATE TABLE open (timestamp bigint(20), open double)"
        self.test_handler.create_table(sql)


if __name__ == '__main__':
    unittest.main()

#    self.assertEqual(len(create_num_list(10)), 10)
