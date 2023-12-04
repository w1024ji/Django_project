# forecast/services.py

import requests

def get_weather_data(api_url, api_key, params):
    url = f"{api_url}?serviceKey={api_key}"

    # 요청에 헤더도 넣음
    headers = {
        'Content-Type': 'application/json',
    }

    # get으로 요청
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # 딕셔너리로 리턴
        return response.json()
    else:
        print('response.status_code != 200 in services.py')
        return None