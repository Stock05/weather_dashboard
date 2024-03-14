from datetime import datetime, timedelta
import json
import requests
import json
from dotenv import load_dotenv
import os


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


def get_data():
    temperature = data['list']['main']['temp']




    