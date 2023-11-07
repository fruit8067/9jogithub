import requests
import json
from datetime import datetime

'''
초단기 실황 
1시간마다 날씨 정보를 매시간 40분에 업데이트함

초단기 예보


(초단기 실황은 그 시간 날씨 정보, 초단기 예보는 1시간 뒤 예측)

단기 예보 
1일 8회 02:00, 05:00, ..., 23:00시 날씨 정보 제공, 업뎃은 02:10, 05:10, ..., 23:10시 간격으로


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

# (시/도, x, y) -> 위경도를 xy로 바꿔서 입력, 참고 : (위경도 찾기)http://map.esran.com, (위경도 to xy)https://fronteer.kr/service/kmaxy 
cities = [('kimhae', 95, 77), ('other_city', 0, 0)]

# 기상청 api
service_key = 'CCXilN3f875IpMsuU1XfkYU4iyxJTpmqCYlbxiaqwkMuNZ3hlWsfqnZ7P3BYNWoaFbudRMViAUpYp7IfhFaJ2w=='

# 초단기 실황
url_ultra_N = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

# 초단기 예보
url_ultra_F = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'

# 단기 예보
url_vilage = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'

class Weather:
    def __init__(self, city_num, url):
        params = {
            'serviceKey': service_key,
            'pageNo': '1',
            'numOfRows': '10',
            'dataType': 'JSON',
            'base_date': datetime.today().strftime("%Y%m%d"),
            'base_time': '0600',
            'nx': cities[city_num][1],
            'ny': cities[city_num][2]
        }

        self.response = requests.get(url, params=params, verify=False)
        self.res_json = json.loads(self.response.text)

    def set_weather_state(self):
        return self.response.text

    def set_weather_temperature(self):
        return 0

    def get_weather_state(self):
        return self.state

    def get_weather_temperature(self):
        return self.temperature

weather = Weather(0)
weather_state = weather.set_weather_state()
print(weather_state)