# forecast/views.py

from django.shortcuts import render
from .services import get_weather_data
from .models import Weather
import os

def fetch_and_save_weather(request):
    api_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
    api_key = os.getenv('API_KEY', '')

    params = {
        'numOfRows': 10,
        'dataType': 'JSON',
        'pageNo': 1,
        'base_date': '20231116',
        'base_time': '2035',
        'nx': 61,
        'ny': 128,
    }

    # Fetch data from the API
    response = get_weather_data(api_url, api_key, params)

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

            return render(request, 'success.html', {'message': 'Data fetched and saved successfully!', 'items': items})
    
    return render(request, 'error.html', {'message': 'Failed to fetch data from the API.'})
