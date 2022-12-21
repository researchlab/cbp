import streamlit as st 

st.set_page_config(layout="wide")
col1,col2,col3,col4,col5 = st.columns([0.2,1,0.2,1,0.2])
# st.empty() 用于留白区域
with col1:
    st.empty()
with col2:
    # 这里放第1，2个图表代码
with col3:
    st.empty()
with col4:
    # 这里放第3，4个图表代码
with col5:
    st.empty()
