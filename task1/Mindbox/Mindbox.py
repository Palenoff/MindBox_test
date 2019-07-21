import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def join_tables():
	order_lines = pd.read_csv("order_lines.csv")
	orders = pd.read_csv("orders.csv")
	return order_lines.join(orders.set_index("OrderId"),on="OrderId")

def get_report(df):
	end_date = datetime.today()
	 #под последним месяцем я понимаю промежуток времени между сегодняшним днём и днём, который был 30 дней назад
	start_date = end_date - timedelta(days=30)
	df.set_index(['DateTime'])
	correct_dates_df = df[df['DateTime'].between(str(start_date),str(end_date))] #выбрали только те строки ,которые попадают в промежуток
	correct_dates_df.set_index('ProductId')
	report = correct_dates_df.groupby('ProductId').\
        agg(count=('OrderId','count'),sum=('Price','sum'),avg=('Price','mean')).reset_index() #такое именование столбцов в отчёте при агрегации возможно только в padnas>=0.25
	return report

df = join_tables()
print(df)
get_report(df)