import requests
import json
from dotenv import load_dotenv
import os
from utility import * 
import streamlit as st
import pandas as pd



call_api(37.5,127.0)
data_kor = read_json('data_kor.json')

#trans_kor_time('data.json')
st.header("날씨 정보 대시보드")
st.info("위도와 경도를 입력해 날씨를 알수 있습니다")

data_list = make_df(data_kor)
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