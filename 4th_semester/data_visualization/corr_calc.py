import pandas as pd

if __name__ == '__main__':
    apple_df = pd.read_csv('AAPL.csv').set_index('Date')
    bitcoin_df = pd.read_csv('BTC-USD.csv').set_index('Date')
    eth_df = pd.read_csv('ETH-USD.csv').set_index('Date')
    google_df = pd.read_csv('GOOG.csv').set_index('Date')
    TSLA_df = pd.read_csv('TSLA.csv').set_index('Date')

    # do the joins
    this_df = apple_df.join(bitcoin_df, on = 'Date', lsuffix = '_apple', rsuffix = '_bitcoin', how = 'inner')
    print(this_df.head())
    print(this_df.columns)
    stock1_l, stock2_l, correlation_l = [], [], []
    this_df = this_df.join(eth_df, on = 'Date', rsuffix = '_ether', how = 'inner')
    this_df = this_df.join(google_df, on = 'Date', rsuffix = '_google', how = 'inner')
    this_df = this_df.join(TSLA_df, on = 'Date', rsuffix = '_tesla', how = 'inner')
    column_list = ['Close_apple', 'Close_bitcoin', 'Close', 'Close_google', 'Close_tesla']
    stock_list = ['Apple', 'BitCoin', 'Ethereum', 'Google', 'Tesla']

    this_df = this_df.reset_index(level = 0)
    this_df = this_df[this_df['Date'] > '2016-01-01']    
    for col_1, stock1 in zip(column_list, stock_list):
        for col_2, stock2 in zip(column_list, stock_list):
            stock1_l.append(stock1)
            stock2_l.append(stock2)
            correlation_l.append(this_df[col_1].corr(this_df[col_2]))

    corr_df = pd.DataFrame({'Stock1': stock1_l, 'Stock2': stock2_l, 'Correlation': correlation_l})
    corr_df.to_csv('stock_correlation.csv', index = False)
    print(this_df.reset_index(level = 0)['Date'].min())