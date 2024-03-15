import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
from utility import *
from matplotlib.cm import get_cmap
import json
import random



tab10 = get_cmap('tab10') #'tab10' 컬러맵은 10개의 구분된 색상을 가진 컬러맵으로, 다양한 데이터를 구분하여 시각화할 때 사용

path = "data_kor.json"  #파일의 경로

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data_kor = read_json('data_kor.json')
data_list = make_df(data_kor)
df = pd.DataFrame(data_list)
tmp = df.copy()

#하단 데이터에 대한 설명
st.title("항목별 데이터")
st.subheader('날짜에 따른 데이터')
st.write('')

#데이터 가공
col = st.selectbox('분석 컬럼 선택',tmp.columns[1:-1]) # 드롭다운 박스 제공 
whole_values = tmp.groupby('날짜')[[col]].mean() # 연령 코드로 그룹화된 값을 드롭다운 박스에서 선택된 값으로 평균을 구함
#st.download_button('Download',whole_values.to_csv(encoding='euc-kr'), '날짜별 데이터.csv') # whole_values값을 다운로드하는 버튼 제공

colors = [tab10(random.randint(0, 9))] # 
prev_date = None
for date in df['날짜']:
    hour = int(date[11:13])
    if hour == 21 and prev_date != date:
        colors.append(tab10.colors[len(colors) % 10])
    else:
        colors.append(colors[-1])
    prev_date = date



#그래프 생성
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글이 깨지는것을 막기위한 한글 지원 폰트 설정
fig, ax = plt.subplots()
ax.set_title(col) # 제목값을 col로 설정
ax.bar(whole_values.index.astype(str), whole_values[col], color=colors) # x,y 값 설정
plt.xticks(df['날짜'], [date[11:13] for date in df['날짜']])
plt.xticks(fontsize=7)

overall_average = whole_values[col].mean()
ax.axhline(y=overall_average, color='gray', linestyle='--', linewidth=2) # 전체값의 평균점을 -- 라인으로 표시
st.pyplot(fig) # 그래프 출력

