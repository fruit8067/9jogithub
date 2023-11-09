import requests
import json
from datetime import datetime

'''
초단기 실황 
1시간마다 날씨 정보를 매시간 40분에 업데이트함

초단기 예보


(초단기 실황은 그 시간 날씨 정보, 초단기 예보는 1시간 뒤 예측)

단기 예보 
1일 8회 02:00, 05:00, ..., 23:00시 날씨 정보 제공, 업뎃은 02:10, 05:10, ..., 23:10시 간격으로, 최대 3일까지 예보 제공


*기상 정보 기호

[초단기 실황]
T1H 기온
RN1 1시간 강수량
UUU 동서바람성분
VVV 남북바람성분
REH 습도
PTY 강수형태
VEC 풍향
WSD 풍속

[초단기 예보]
T1H 기온
RN1 1시간 강수량
SKY 하늘상태
UUU 동서바람성분
VVV 남북바람성분
REH 습도
PTY 강수형태
LGT 낙뢰
VEC 풍향
WSD 풍속

[단기 예보]
POP 강수확률
PTY 강수형태
PCP 1시간 강수량
REH 습도
SNO 1시간 신적설
SKY 하늘상태
TMP 1시간 기온
TMN 일 최저기온
TMX 일 최고기온
UUU 풍속(동서성분)
VVV 풍속(남북성분)
WAV 파고
VEC 풍향
WSD 풍속
'''

# 각 문자열은 내가 기상청에 있는거 토대로 임의로 정한거니까 어색하면 바꿔도 돼
sky_code = {1 : '맑음', 3 : '구름 많음', 4 : '흐림'}
pty_code = {0 : '강수 없음', 1 : '비', 2 : '비/눈', 3 : '눈', 4 : '소나기', 5 : '빗방울', 6 : '빗방울눈날림', 7 : '눈날림'}

# (시/도, x, y) -> 위경도를 xy로 바꿔서 입력, 참고 : (위경도 찾기)http://map.esran.com, (위경도 to xy)https://fronteer.kr/service/kmaxy 
cities = [('kimhae', 95, 77), ('other_city', 0, 0)]

# 기상청 api
service_key = 'CCXilN3f875IpMsuU1XfkYU4iyxJTpmqCYlbxiaqwkMuNZ3hlWsfqnZ7P3BYNWoaFbudRMViAUpYp7IfhFaJ2w=='

# 초단기 실황
url_ultra_N = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

# 초단기 예보
url_ultra_F = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

# 단기 예보
url_vilage = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'

class Weather:
    def __init__(self, city_num, url, time):
        param = {
            'serviceKey': service_key,
            'pageNo': '1',
            'numOfRows': '60',
            'dataType': 'JSON',
            'base_date': datetime.today().strftime("%Y%m%d"),
            'base_time': time,
            'nx': cities[city_num][1],
            'ny': cities[city_num][2]
        }

        self.response = requests.get(url, params=param)
        self.res_json = json.loads(self.response.text)

        self.temperature = self.set_weather_temperature()
        self.sky = sky_code[int(self.set_weather_sky())]
    '''
    자주 쓰이는 날씨 정보는 set_weather_xxx 함수로 미리 지정하는게 최적화에 좋음, 
    잘 안쓰이면 저거 할 필요없이 그냥 get_weather_xxx 함수 호출할 때마다 불러오게 하면 돼
    '''
    def set_weather_sky(self):
        for i in self.res_json['response']['body']['items']['item']:
            if(i['category'] == 'SKY'):
                return (i['fcstValue'])

    def set_weather_temperature(self):
        for i in self.res_json['response']['body']['items']['item']:
            if(i['category'] == 'T1H'):
                return i['fcstValue']

'''
사용법

# 일단 url_ultra_F가 기본값
weather = Weather(0,url_ultra_F,'1230')

# 날씨 상태 EX) 맑음, 흐림, ..
print(weather.sky)

# 기온 (숫자만 나옴)
print(weather.temperature)
'''            