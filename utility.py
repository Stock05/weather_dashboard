from datetime import datetime, timedelta
import json
import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
import streamlit as st


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