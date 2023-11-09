import requests
import json
from datetime import datetime
url = "https://open.neis.go.kr/hub/mealServiceDietInfo"

service_key = "1aca86770d994a46aa72b9f94f2ba07e"

params = {
    'KEY' : service_key,
    'Type' : 'json',
    'pIndex' : '1',
    'pSize' : '100',
    'ATPT_OFCDC_SC_CODE' : 'S10',
    'SD_SCHUL_CODE' : '9010041',
    "MLSV_FROM_YMD": datetime.today().strftime("%Y%m%d"),
    "MLSV_TO_YMD" : datetime.today().strftime("%Y%m%d")
}

response = requests.get(url, params=params)
print(response)

def find_meal():
    try:
        j_response = json.loads(response.text)["mealServiceDietInfo"]
        if j_response[0]["head"][0]["list_total_count"] == 1:
            return j_response[1]["row"][0]
        else:
            return j_response[1]["row"]
    except:
        print("찾는 데이터가 없습니다.")
        return response.text


def meal(x):
    data = find_meal()
    try:
        if x == 0:
            string = "<중식>\n" + data[0]["DDISH_NM"].replace("<br/>", "\n") + "\n\n"
        else:
            string = "<석식>\n" + data[1]["DDISH_NM"].replace("<br/>", "\n")
        characters = "1234567890./-*()"
        for x in range(len(characters)):
            string = string.replace(characters[x], "")
        return string
    except:
        return "오늘은 급식이 없습니다."
