# forecast/services.py

import requests
import time

def get_weather_data(api_url, api_key, params):
    start_time = time.time()  # Record the start time

    url = f"{api_url}?serviceKey={api_key}"

    # 요청에 헤더도 넣음
    headers = {
        'Content-Type': 'application/json',
    }

    # get으로 요청
    response = requests.get(url, headers=headers, params=params)


    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f"API request에 걸린 시간(services.py): {elapsed_time} seconds")

    if response.status_code == 200:
        # 딕셔너리로 리턴
        return response.json()
    else:
        print('response.status_code != 200 in services.py')
        return None