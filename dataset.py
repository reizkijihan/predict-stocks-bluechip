import streamlit as st
from datetime import date
import yfinance as yf 
from plotly import graph_objs as go

def app():
    st.markdown(f"<h1 style='text-align: center;'>History's Data Set Blue Chip</h1>",unsafe_allow_html=True)

    image = st.image('buy-stocks.jpg')

    START = "2022-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    stocks = ('BBCA.JK', 'BBRI.JK', 'UNVR.JK', 'TLKM.JK', 'ICBP.JK', 'BMRI.JK', 'PGAS.JK', 'ASII.JK', 'BBNI.JK', 'UNTR.JK', 'ANTM.JK', 'GGRM.JK', 'HMSP.JK','ICBP.JK', 'MYOR.JK')
    selected_stock = st.selectbox('Select Data', stocks)

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_stock)
    st.success("Loading Data Done!")

    st.subheader('Data Set')
    st.write(data)

    # Plot raw data
    def plot_raw_data():
	    fig = go.Figure()
	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Adj Close'], name="stock_adjclose"))
	    fig.add_trace(go.Scatter(x=data['Date'], y=data['High'], name="stock_high"))
	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Low'], name="stock_low"))
	    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	    st.plotly_chart(fig)
	
    plot_raw_data()
    
