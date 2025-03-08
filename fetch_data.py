import tushare as ts
def fetch_data(stock_code='st_code',start_date='start_date',end_date='end_date'):
    pro=ts.api('st_code',tokens='')
    df=pro.
if __name__ == '__main__':
df=fetch_data('300115.SZ',20250310,20250310)
df.to_csv('data_fetch.csv')
