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

    # nx, ny는 덕성여대로 위치 고정
    # numOfRows=40와 pageNo=1로 해야 한 페이지에 전체 데이터가 나온다
    params = {
        'numOfRows': 40,
        'dataType': 'JSON',
        'pageNo': 1,
        'base_date': base_date,
        'base_time': base_time,
        'nx': 61,
        'ny': 128,
    }

    # services.py의 get_seather_data()를 가져와 딕셔너리 형태로 받기
    response = get_weather_data(api_url, api_key, params)

    if response and 'response' in response and 'body' in response['response']:
        # 데이터에 접근하려면 ['response']['body']['items']['item']안쪽으로 접근해야 한다
        items = response['response']['body']['items']['item']
        
        if items:
            for item in items:
                # 인스턴스 만들고 데베에 추가
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

            # T1H(기온), SKY(하늘상태), PTY(강수형태)의 데이터를 필터링한다
            desired_categories = {'T1H', 'SKY', 'PTY'}
            filtered_items = [item for item in items if item.get('category') in desired_categories]

            # 날짜와 시간을 기준으로 T1H, SKY, PTY를 묶기
            organized_items = {}
            for item in filtered_items:
                fcst_date = item['fcstDate']
                fcst_time = item['fcstTime']
                key = f"{fcst_date}_{fcst_time}"
                if key not in organized_items:
                    organized_items[key] = []
                organized_items[key].append({'category': item['category'], 'fcstValue': item['fcstValue']})
            

            # Get the earliest date for landing.html
            earliest_date_key = min(organized_items.keys())
            earliest_date_group = organized_items[earliest_date_key]

            # Extract all categories from the earliest date
            earliest_date_categories = [{'category': item['category'], 'fcstValue': item['fcstValue']} for item in earliest_date_group]

            earliest_date = {
                'date_time': earliest_date_key,
                'categories': earliest_date_categories,
            }
            

        # Render landing.html with the necessary data
        return render(request, 'forecast/landing.html', {
            'message': 'Data fetched and saved successfully!',
            'organized_items': organized_items,
            'earliest_date': earliest_date
        })
    
    return render(request, 'error.html', {'message': 'Failed to fetch data from the API.'})



from django.shortcuts import get_object_or_404
from .models import Poll

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'forecast/poll_detail.html', {'poll': poll})


#  View for Voting

from django.http import JsonResponse
from .models import Choice
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def vote(request):
    if request.method == 'POST':
        choice_id = request.POST.get('choice_id')
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes += 1
        choice.save()
        return JsonResponse({'votes': choice.votes})
    # Handle other HTTP methods if needed
    return JsonResponse({'error': 'Invalid request method'})