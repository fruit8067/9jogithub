import customtkinter
import tkinter
#meal.meal(0) -> 오늘의 점심, meal.meal(1) -> 오늘의 저녁을 리턴
import meal

from datetime import datetime


def find_subject(current_day, current_hour):
    # 요일과 교시에 따라 과목을 매핑하는 딕셔너리
    schedule = {
        '월요일': {
            1: '체육',
            2: 'A',
            3: 'B',
            4: '창체',
            5: '독서',
            6: 'C',
            7: '수학',
        },
        '화요일': {
            1: '독서',
            2: '수학',
            3: 'C',
            4: 'C',
            5: '일본어',
            6: '영어',
            7: '음악',
        },
        '수요일': {
            1: 'B',
            2: 'B',
            3: '영어',
            4: 'A',
            5: '창체',
            6: '창체',

        },
        '목요일': {
            1: '체육',
            2: 'B',
            3: '영어',
            4: '음악',
            5: 'A',
            6: 'A',
            7: '수학',
        },
        '금요일': {
            1: '독서',
            2: '독서',
            3: '영어',
            4: '진로',
            5: 'C',
            6: '수학',
            7: '일본어',
        }
    }
    if current_day in schedule and current_hour in schedule[current_day]:
        return schedule[current_day][current_hour]
    else:
        return "해당 요일과 교시에는 과목이 없습니다."


# 학교 시간표
school_schedule = [
    ("1교시", "08:45", "09:35"),
    ("2교시", "09:45", "10:35"),
    ("3교시", "10:45", "11:35"),
    ("4교시", "11:45", "12:35"),
    ("점심", "12:35", "13:25"),
    ("5교시", "13:35", "14:25"),
    ("6교시", "14:35", "15:25"),
    ("청소", "15:25", "15:40"),
    ("7교시", "15:40", "16:30"),
    ("8교시", "16:40", "17:40"),
    ("저녁", "17:40", "18:30"),
]


# 최적화 한번
def get_current_school_period(schedule):
    # 현재 시간 구하기
    now = datetime.now().time()

    ans = ''
    for period, start_time, end_time in schedule:
        start = datetime.strptime(start_time, "%H:%M").time()
        end = datetime.strptime(end_time, "%H:%M").time()

        if start <= now <= end:
            ans = period

        elif now >= end:
            if period == '저녁':
                ans = period + "이 지남"
            else:   ans = f"{period} 쉬는시간"
    return ans



current_period = get_current_school_period(school_schedule)
print(f"현재 {current_period}입니다.")



def current_subject():
    try:
        t = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        day = t[datetime.today().weekday()]
        current_period = get_current_school_period(school_schedule)


        if len(current_period) > 4:
            current_period = str((int(current_period[0]) + 1)) + "교시"
            return "다음교시 : " + find_subject(day, int(current_period[0]))
        else:
            return find_subject(day,int(current_period[0]))
    except:
        print(get_current_school_period(school_schedule))



print(current_subject())


customtkinter.set_appearance_mode("dark") # 태마 // 버튼 색깔
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk() #실행 설정
app.title("Custom App by 9's group") # 이름 변경하고 싶으면 말하셈
app.geometry("640x480")

my_font = customtkinter.CTkFont(family="Noto Sans KR Medium", size=30) # 저기 파일에서 폰트 다운 받으셈


#탭 생성, 과목, 밥, 날씨 탭 생성, 초기에는 과목 보여주기
tabView = customtkinter.CTkTabview(app, width=640, height=480, corner_radius=10)
tabView.add("Subject")
tabView.add("Meal")
tabView.add("Weather")
tabView.set("Subject")
tabView._segmented_button.configure(font=my_font)
tabView.pack(padx=20, pady=10)



#과목 진행바, 택스트 설정
progressbar = customtkinter.CTkProgressBar(tabView.tab("Subject"), width=500, height=5)
progressbar.set(0)
progressbar.place(relx = 0.5, rely=0.1, anchor = tkinter.CENTER)

#과목 얻기
def get_subject():
    string = current_subject()
    try:
        if len(string) < 4:
            text_subject.configure(text=string)
            text_subject.after(1000,get_subject)
        else:
            text_subject.configure(text=string,  font=customtkinter.CTkFont(family="Noto Sans KR Medium", size=80))
            text_subject.after(1000, get_subject)
    except:
        print(f"에러 발생 string = {string}")
        text_subject.after(1000, get_subject)

text_subject = customtkinter.CTkLabel(tabView.tab("Subject"), width=400, height=100, font=customtkinter.CTkFont(family="Noto Sans KR Medium", size=100 ),fg_color="transparent")
text_subject.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
get_subject()

#시간 봐꾸기
def get_time():
    string = datetime.now().strftime('%H:%M:%S %p')
    Timelbl.configure(text=string)
    Timelbl.after(1000, get_time)

Timelbl = customtkinter.CTkLabel(tabView.tab("Subject"),
                                 font=my_font)
Timelbl.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)
get_time()




#progressbar.set( 0부터 1까지의 실수) -> 진행바 진행 설정 -> 수업시간에는 1분에 1/60만큼, 쉬는시간에는 1분에 1/10만큼 움직여야함 -> 여기 라인에 progressbar.set() 넣어면 됨


#급식
text_meal = customtkinter.CTkTextbox(tabView.tab("Meal"), width=400, height=100, font=my_font)
text_meal.pack(fill="both", expand=True)
text_meal.tag_config("center", justify="center")
text_meal.insert("end", "Hello world", "center") # 여기 Hello world 자리에 급식 넣기


#1교시부터 5교시 시작전까지는 meal.meal(0)을 사용하여 점심을, 5교시부터 야자 2교시까지는 meal.meal(1)을 사용하여 저녁을 보여줘야함
#print(meal.meal(0)) -> 점심 메뉴 보여줌

#날씨

#저기 img 파일에 날씨별로 png파일이 있음 그래서 그냥 김해 날씨 찾는 함수 하나만 만들어주면 내가 한번 만들어봄



app.mainloop()
