import home
import dataset
import forecast
import video
import news
import streamlit as st

PAGES = {
    "Home": home,
    "Dataset": dataset,
    "Prediksi": forecast,
    "Video": video,
    "News": news
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Choice your page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
