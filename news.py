import streamlit as st
import json
import requests 

def app():
    st.markdown(f"<h1 style='text-align: center;'>Hot News Stocks</h1>",unsafe_allow_html=True)

    r = requests.get('https://newsapi.org/v2/top-headlines?country=id&category=business&q=saham&apiKey=4a4bcac0e6544b62b3afec944c3ec303')
    sources = json.loads(r.content)

    for i in range(5):
        news = sources['articles'][i]['title']
        st.header(news)

        image = sources['articles'][i]['urlToImage']
        try:
            st.image(image)
        except:
            pass
        else:
            pass
        publishedAt = sources['articles'][i]['publishedAt']
        st.write(publishedAt)

        content = sources['articles'][i]['content']
        st.write(content)

        url = sources['articles'][i]['url']
        st.write(url)