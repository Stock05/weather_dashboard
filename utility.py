from datetime import datetime, timedelta
import json
import requests
from dotenv import load_dotenv
import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import random

def call_api(lat,lon):
    load_dotenv()
    weather_api_key = os.getenv("WEATHER_API_KEY1")            
    api = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={weather_api_key}&units=metric"
    result = requests.get(api)
    data = json.loads(result.text)
    with open('data.json', 'w') as file:
        json.dump(data, file)
    trans_kor_time(data)      
    print('완료')

def trans_kor_time(data):
    for count in range(len(data['list'])):
        dt_txt = data['list'][count]['dt_txt']    
        kor_time = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S") + timedelta(hours=9)
        data['list'][count]['kor_time'] = kor_time.strftime('%Y-%m-%d %H:%M:%S')
    with open('data_kor.json', 'w') as file:
        json.dump(data, file)

def read_json(filename):
    with open(filename, 'r') as file:                 
        return json.loads(file.read())

def make_df(data_kor):
    data_list=[]    
    for count in range(len(data_kor['list'])):
        temp = data_kor["list"][count]['main']['temp']
        feels_like = data_kor["list"][count]['main']['feels_like']
        temp_min = data_kor["list"][count]['main']['temp_min']
        temp_max = data_kor["list"][count]['main']['temp_max']
        humidity = data_kor["list"][count]['main']['humidity']
        pressure = data_kor["list"][count]['main']['pressure']
        clouds = data_kor["list"][count]['clouds']['all']    
        deg = data_kor["list"][count]['wind']['deg']
        speed = data_kor["list"][count]['wind']['speed']
        weather = data_kor["list"][count]["weather"][0]["description"]
        date = data_kor["list"][count]['kor_time']
        data = {
            '날짜': date,
            '온도': temp,
            '체감온도': feels_like,
            '최저온도': temp_min,
            '최고온도': temp_max,
            '습도': humidity,
            '기압': pressure,
            '구름': clouds,
            '풍향': deg,
            '풍속': speed,
            '날씨': weather
            
        }    
        data_list.append(data)
    return data_list    


def save_coordinate(lat, lon):
    lat = lat
    lon = lon
    return lat, lon


def make_graph():
    tab10 = get_cmap('tab10') #'tab10' 컬러맵은 10개의 구분된 색상을 가진 컬러맵으로, 다양한 데이터를 구분하여 시각화할 때 사용

    path = "data_kor.json"  #파일의 경로
    
    data_kor = read_json('data_kor.json')
    data_list = make_df(data_kor)
    df = pd.DataFrame(data_list)
    tmp = df.copy()

    #하단 데이터에 대한 설명
    st.title("항목별 데이터")
    st.subheader('3시간별 데이터')
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