# forecast/services.py

import requests

def get_weather_data(api_url, api_key, params):

    url = f"{api_url}?serviceKey={api_key}"

    headers = {
        'Content-Type': 'application/json',
    }

    # Include other parameters in the request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        # 나중에 에러 추가하기!
        return None
