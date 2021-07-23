import streamlit as st
import pandas as pd

def app():
    st.markdown(f"<h1 style='text-align: center;'>Welcome to Forecasting Stock Blue Chip</h1>",unsafe_allow_html=True)

    st.markdown('## Forward Dividend & Yield')
    #kpi1

    BBCA, BBNI, BBRI, BMRI = st.beta_columns(4)

    with BBCA:
            st.markdown("**BBCA.JK**")
            number1 = 1.70 
            st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}%</h1>", unsafe_allow_html=True)

    with BBNI:
            st.markdown("**BBNI.JK**")
            number2 = 0.89
            st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}%</h1>", unsafe_allow_html=True)

    with BBRI:
            st.markdown("**BBRI.JK**")
            number3 = 2.51
            st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}%</h1>", unsafe_allow_html=True)

    with BMRI:
            st.markdown("**BMRI.JK**")
            number4 = 3.66
            st.markdown(f"<h1 style='text-align: center; color: red;'>{number4}%</h1>", unsafe_allow_html=True)

    st.markdown("<hr/>",unsafe_allow_html=True)


        # kpi 1 

    ANTM, UNVR, TLKM, ICBP, PGAS = st.beta_columns(5)

    with ANTM:
            st.markdown("**ANTM.JK**")
            number5 = 0.75
            st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number5}%</h1>", unsafe_allow_html=True)

    with UNVR:
            st.markdown("**UNVR.JK**")
            number6 = 3.96
            st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number6}%</h1>", unsafe_allow_html=True)

    with TLKM:
            st.markdown("**TLKM.JK**")
            number7 = 5.09
            st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number7}%</h1>", unsafe_allow_html=True)

    with ICBP:
            st.markdown("**ICBP.JK**")
            number8 = 2.77
            st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number8}%</h1>", unsafe_allow_html=True)

    with PGAS:
            st.markdown("**PGAS.JK**")
            number9 = " "
            st.markdown(f"<h1 style='text-align: center; color: yellow;'>N/A{number9}</h1>", unsafe_allow_html=True)

    st.markdown("<hr/>",unsafe_allow_html=True)

    ASII, UNTR, GGRM, HMSP, MYOR, INDF = st.beta_columns(6)

    with ASII:
            st.markdown("**ASII.JK**")
            number10 = 2.32
            st.markdown(f"<h1 style='text-align: center; color: blue;'>{number10}%</h1>", unsafe_allow_html=True)
    with UNTR:
            st.markdown("**UNTR.JK**")
            number11 = 2.98 
            st.markdown(f"<h1 style='text-align: center; color: blue;'>{number11}%</h1>", unsafe_allow_html=True)
    with GGRM:
            st.markdown("**GGRM.JK**")
            number12 = " "
            st.markdown(f"<h1 style='text-align: center; color: blue;'>N/A{number12}</h1>", unsafe_allow_html=True)
    with HMSP:
            st.markdown("**HMSP.JK**")
            number13 = 6.47
            st.markdown(f"<h1 style='text-align: center; color: blue;'>{number13}%</h1>", unsafe_allow_html=True)
    with MYOR:
            st.markdown("**MYOR.JK**")
            number14 = 1.28
            st.markdown(f"<h1 style='text-align: center; color: blue;'>{number14}%</h1>", unsafe_allow_html=True)
    with INDF:
            st.markdown("**INDF.JK**")
            number5 = 4.61
            st.markdown(f"<h1 style='text-align: center; color: blue;'>{number5}%</h1>", unsafe_allow_html=True)

    st.markdown("## Chart Blue Chip")

    @st.cache
    def load_data(nrows):
            data = pd.read_csv('dataset.csv', nrows=nrows)
            return data
            
    data_stocks = load_data(1000)

    chart_data1 = pd.DataFrame(data_stocks,columns=['BBCA', 'BBNI', 'BBRI', 'BMRI', 'ANTM', 'UNVR', 'TLKM', 'ICBP', 'PGAS', 'ASII', 'UNTR', 'GGRM', 'HMSP', 'MYOR', 'INDF'])
    st.line_chart(chart_data1)