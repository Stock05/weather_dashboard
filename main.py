import requests
import json
from dotenv import load_dotenv
import os
from utility import * 
import streamlit as st
import pandas as pd



call_api(37.5,127.0)
data_kor = read_json('data_kor.json')
st.header("날씨 정보 대시보드")
st.info("위도와 경도를 입력해 날씨를 알수 있습니다 (기본 서울)")
data_list = make_df(data_kor)
df = pd.DataFrame(data_list)
pd.set_option('display.float_format', '{:.2f}'.format)
st.dataframe(df, hide_index=True)


