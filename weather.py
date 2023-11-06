import requests
import json
from datetime import datetime

weather_list = [('Rain', 0), ('Snow', 1), ('Sun', 2), ('Thunderstorm', 3), ('Wind', 4)]

# (시/도, x, y) -> 위경도를 xy로 바꿔서 입력
# 참고 : (위경도 찾기)http://map.esran.com, (위경도 to xy)https://fronteer.kr/service/kmaxy 
cities = [('kimhae', 95, 77), ('other_city', 0, 0)]

# 기상청 api
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
service_key = "CCXilN3f875IpMsuU1XfkYU4iyxJTpmqCYlbxiaqwkMuNZ3hlWsfqnZ7P3BYNWoaFbudRMViAUpYp7IfhFaJ2w%3D%3D"

params = {'serviceKey' : service_key, 
          'pageNo' : '1',
          'numOfRows' : '1000',
          'dataType' : 'JSON',
          'base_date' : datetime.today().strftime("%Y%m%d"), # 현재 날짜
          'base_time' : '0600', # 고정
          'nx' : cities[0][1], # x 좌표
          'ny' :  cities[0][2]# y 좌표
}

response = requests.get(url, params=params, verify=False)
print(response)

class Weather:
    state = 0
    temperature = 0

    def __init__(self):
        self.state = self.get_weather_state()
        self.temperature = self.get_weather_temperature()
    
    def get_weather_state(self):
        return self.state
    
    def get_weather_temperature(self):
        return self.temperature