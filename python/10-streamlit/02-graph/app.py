import streamlit as st
import pandas as pd 
import numpy as np 
import time

df = pd.DataFrame({
    'first':[5,6,7,8,9]
    })
# 绘制折线图

chart_data = pd.DataFrame(np.random.randn(20,3),
        columns=['a','b','c'])

st.line_chart(chart_data)

# 地图
map_data = pd.DataFrame(
        np.random.randn(1000,2)/[50,50]+[32.37,118.4],
        columns=['lat','lon']
        )

st.map(map_data)

# checkbox 
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
            np.random.randn(20,3),
            columns=['a','b','c']
            )
    chart_data

# selectbox
# st.sidebar 表示放到侧边
# st.sidebar.markdown(), st.sidebar.slider(), st.sidebar.line_chart()
option = st.sidebar.selectbox(
        'Which number do you like best?',
        df['first']
        )

'You selected:',option


# 可以使用st.beta_columns来并排布置小部件，或者使用st.beta_expander来隐藏大型内容以节省空间。

left_column, right_column = st.columns(2)

pressed = left_column.button('Press me')
if pressed:
    right_column.write('woohoo')

expander = st.expander('FAQ')
expander.write('Here you could put in some really, really long explanations.')

# progress 

# add a placeholder
latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'...and now done'
