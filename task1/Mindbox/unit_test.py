import unittest
import Mindbox
import pandas as pd
import numpy as np

class Test_unit_test(unittest.TestCase):
    def setUp(self):
        self.table = pd.DataFrame(data={"ProductId":[5873,7265,9675,5873,13,274,274],
										 "OrderId":[5,5,5,6,6,79,32],
										 "Price":[3026.0,573.0,159.0,2999.0,57.0,27.0,298.0],
										 "CustomerId":[583.0,583.0,583.0,np.nan,np.nan,9954.0,1258.0],
										 "DateTime":["2019-07-01 15:03:17","2019-07-01 15:03:17","2019-07-01 15:03:17",np.nan,np.nan,"2019-06-30 09:30:28","2019-06-25 09:30:28"]})
        self.report = pd.DataFrame(data={"ProductId":[274,5873,7265,9675],
										 "count":[2,1,1,1],
										 "sum":[325.0,3026.0,573.0,159.0],
										 "avg":[162.5,3026.0,573.0,159.0]})

    def test_join(self): #тест на проверку правильности соединения таблиц
        join = Mindbox.join_tables()
        pd.testing.assert_frame_equal(self.table,join)

    def test_report(self): #тест на корректность отчёта
        report = Mindbox.get_report(self.table)
        pd.testing.assert_frame_equal(self.report,report)

if __name__ == '__main__':
    unittest.main()
