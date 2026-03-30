# app.py

import streamlit as st
import matplotlib.pyplot as plt
from prediction import predict_stock


# TITLE

st.title("📈 Stock Price Prediction App")


# USER INPUT


stock = st.text_input("Enter Stock Symbol (e.g., TCS.NS)", "TCS.NS")

days = st.number_input(
    "Enter number of days to predict",
    min_value=1,
    max_value=60,
    value=30
)



if st.button("Predict"):

    try:
        # Call prediction function
        data, future_df = predict_stock(stock, days)

       
        # SHOW HISTORICAL DATA
     
        st.subheader("📊 Historical Stock Data")

        fig1, ax1 = plt.subplots()
        ax1.plot(data.index, data['Close'])
        ax1.set_title(f"{stock} Stock Price")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Price")
        plt.xticks(rotation=45)

        st.pyplot(fig1)

      
    
       
        st.subheader("🔮 Future Prediction")

        fig2, ax2 = plt.subplots()
        ax2.plot(future_df.index, future_df['Predicted'], marker='o')
        ax2.set_title(f"Next {days} Days Prediction")
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Price")
        plt.xticks(rotation=45)

        st.pyplot(fig2)

      

       
        st.subheader("📌 Predicted Values")
        st.write(future_df)

    except Exception as e:
        st.error(f"Error: {e}")
