# prediction.py

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def predict_stock(stock, days):
   

    # STEP 1: Download stock data
    data = yf.download(stock, start="2023-01-01")

    # Fix multi-index columns if present
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    # Keep only Close price
    data = data[['Close']].dropna()

    # STEP 2: Prepare data for training
    data['Prediction'] = data['Close'].shift(-days)

    X = np.array(data[['Close']])[:-days]
    y = np.array(data['Prediction'])[:-days]

    # STEP 3: Train model
    model = LinearRegression()
    model.fit(X, y)

    # STEP 4: Predict future prices
    x_future = np.array(data[['Close']])[-days:]
    prediction = model.predict(x_future)

    # STEP 5: Create future dates
    future_dates = pd.date_range(start=data.index[-1], periods=days+1)[1:]

    # Create prediction dataframe
    future_df = pd.DataFrame({
        'Date': future_dates,
        'Predicted': prediction
    })

    future_df.set_index('Date', inplace=True)

    # RETURN results (important for UI)
    return data, future_df