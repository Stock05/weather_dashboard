import requests
import json
from dotenv import load_dotenv
import os
from utility import * 
import streamlit as st
import pandas as pd

lat = None
lon = None

# Streamlit 앱의 타이틀 설정
st.title('주소를 위도와 경도로 변환하기 (Nominatim 사용)')

# 사용자로부터 주소 입력 받기
address = st.text_input('주소를 입력하세요:', '')

# 주소를 위도와 경도로 변환하는 함수
def geocode_address(address):
    # Nominatim API URL
    url = f'https://nominatim.openstreetmap.org/search?format=json&q={address}'
    
    # 사용자 에이전트와 연락처 정보 설정 (Nominatim의 요구사항)
    headers = {
        'User-Agent': 'weather_map asd@gmail.com'
    }
    
    # API 요청
    response = requests.get(url, headers=headers)
    
    # 응답 데이터에서 위도와 경도 추출
    if response.status_code == 200:
        result = response.json()
        if result:
            location = result[0]            
            return location['lat'], location['lon']
            
            
        else:
            return None, None
    else:
        return None, None



# 변환 버튼
if st.button('변환하기'):
    lat, lon = geocode_address(address)    
    if lat is not None and lon is not None:
        st.success(f'위도: {lat}, 경도: {lon}')
    else:
        st.error('위도와 경도를 찾을 수 없습니다. 주소를 확인해 주세요.')



if lat != None and lon != None:
    call_api(lat,lon)
    data_kor = read_json('data_kor.json')    
    st.header("날씨 정보 대시보드")
    st.info("위도와 경도를 입력해 날씨를 알수 있습니다")
    data_list = make_df(data_kor)
    df = pd.DataFrame(data_list)
    pd.set_option('display.float_format', '{:.2f}'.format)
    st.dataframe(df, hide_index=True)   
    make_graph()

    st.session_state['selected_address'] = address   
else:     
    st.text("데이터를 먼저 로드해주세요.")           


# 이전에 선택한 주소가 있다면, 세션 상태에서 가져와 다시 설정
if 'selected_address' in st.session_state:
    address = st.session_state['selected_address']    
    make_graph()

