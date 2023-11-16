# forecast/views.py

from django.shortcuts import render
from .services import get_weather_data
from .models import Weather
import os
from datetime import datetime, timedelta, date


def fetch_and_save_weather(request):
    api_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
    api_key = os.getenv('API_KEY', '')

    now = datetime.now()
    today = datetime.today().strftime("%Y%m%d")
    y = date.today() - timedelta(days=1)
    yesterday = y.strftime("%Y%m%d")
    
    if now.minute<45: # base_time와 base_date 구하는 함수
        if now.hour==0:
            base_time = "2330"
            base_date = yesterday
        else:
            pre_hour = now.hour-1
            if pre_hour<10:
                base_time = "0" + str(pre_hour) + "30"
            else:
                base_time = str(pre_hour) + "30"
            base_date = today
    else:
        if now.hour < 10:
            base_time = "0" + str(now.hour) + "30"
        else:
            base_time = str(now.hour) + "30"
        base_date = today

    # print(base_time) # 성공

    params = {
        'numOfRows': 40,
        'dataType': 'JSON',
        'pageNo': 1,
        'base_date': base_date,
        'base_time': base_time,
        'nx': 61,
        'ny': 128,
    }

    
    response = get_weather_data(api_url, api_key, params)

    # print(response) # 성공

    
    if response and 'response' in response and 'body' in response['response']:
        
        items = response['response']['body']['items']['item']

       

        if items:
            for item in items:
                Weather.objects.create(
                    base_date=item.get('baseDate', ''),
                    base_time=item.get('baseTime', ''),
                    category=item.get('category', ''),
                    fcst_date=item.get('fcstDate', ''),
                    fcst_time=item.get('fcstTime', ''),
                    fcst_value=item.get('fcstValue', ''),
                    nx=item.get('nx', 0),
                    ny=item.get('ny', 0),
                )

            
            desired_categories = {'T1H', 'SKY', 'PTY'}
            filtered_items = [item for item in items if item.get('category') in desired_categories]

        # print(filtered_items) # 성공


        return render(request, 'success.html', {'message': 'Data fetched and saved successfully!', 'filtered_items': filtered_items})
    
    return render(request, 'error.html', {'message': 'Failed to fetch data from the API.'})
