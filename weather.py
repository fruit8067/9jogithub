import requests
import json
from datetime import datetime

weather_list = ['Rain','Snow', 'Sun', 'Thunderstorm', 'Wind']

# (시/도, x, y) -> 위경도를 xy로 바꿔서 입력
# 참고 : (위경도 찾기)http://map.esran.com, (위경도 to xy)https://fronteer.kr/service/kmaxy 
cities = [('kimhae', 95, 77), ('other_city', 0, 0)]

# 기상청 api
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
service_key = "CCXilN3f875IpMsuU1XfkYU4iyxJTpmqCYlbxiaqwkMuNZ3hlWsfqnZ7P3BYNWoaFbudRMViAUpYp7IfhFaJ2w=="

class Weather:
    def __init__(self, city_num):
        params = {
            'serviceKey': service_key,
            'pageNo': '1',
            'numOfRows': '1000',
            'dataType': 'JSON',
            'base_date': datetime.today().strftime("%Y%m%d"),
            'base_time': '0600',
            'nx': cities[city_num][1],
            'ny': cities[city_num][2]
        }

        self.response = requests.get(url, params=params, verify=False)


        self.state = self.set_weather_state()
        self.temperature = self.set_weather_temperature()

    def set_weather_state(self):
        return self.response.content

    def set_weather_temperature(self):
        return 0

    def get_weather_state(self):
        return self.state

    def get_weather_temperature(self):
        return self.temperature

weather = Weather(0)
weather_state = weather.get_weather_state()
print(weather_state)