import requests
import json
from dotenv import load_dotenv
import os
from utility import * 
import streamlit as st
import pandas as pd


call_api(37.5,127.0)
data_kor = read_json('data_kor.json')
print(data_kor)
#trans_kor_time('data.json')
st.header("날씨 정보 대시보드")
st.info("위도와 경도를 입력해 날씨를 알수 있습니다")


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




df = pd.DataFrame(data_list)
pd.set_option('display.float_format', '{:.2f}'.format)
st.dataframe(df, hide_index=True)






    
    







# print(data["name"],"의 날씨입니다.")
# print("날씨는 ",data["weather"][0]["description"],"입니다.")
# print("현재 온도는 ",data["main"]["temp"],"입니다.")
# print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# print("습도는 ",data["main"]["humidity"],"입니다.")
# print("기압은 ",data["main"]["pressure"],"입니다.")
# print("풍향은 ",data["wind"]["deg"],"입니다.")
# print("풍속은 ",data["wind"]["speed"],"입니다.")