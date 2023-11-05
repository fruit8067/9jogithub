import customtkinter
import tkinter
#meal.meal(0) -> 오늘의 점심, meal.meal(1) -> 오늘의 저녁을 리턴
import meal

from datetime import datetime

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

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Custom App by 9's group")
app.geometry("640x480")

my_font = customtkinter.CTkFont(family="Noto Sans KR Medium", size=30, )



tabView = customtkinter.CTkTabview(app, width=640, height=480, corner_radius=10)
tabView.add("Subject")
tabView.add("Meal")
tabView.add("Whether")
tabView.set("Subject")
tabView.pack(padx=20, pady=10)



#과목
progressbar = customtkinter.CTkProgressBar(tabView.tab("Subject"), width=500, height=5)
progressbar.set(0)
progressbar.place(relx = 0.5, rely=0.1, anchor = tkinter.CENTER)
text_subject = customtkinter.CTkTextbox(tabView.tab("Subject"), width=400, height=300, font=customtkinter.CTkFont(family="Noto Sans KR Medium", size=200 ),fg_color="transparent")
text_subject.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
text_subject.tag_config("center", justify="center")
text_subject.insert("0.0", "과목", "center") # 여기 과목 자리에 현재 시각 과목 넣기, 쉬는시간에는 다음 과목 보여주기

#progressbar.set( 0부터 1까지의 실수) -> 진행바 진행 설정 -> 수업시간에는 1분에 1/60만큼, 쉬는시간에는 1분에 1/10만큼 움직여야함
#

#급식
text_meal = customtkinter.CTkTextbox(tabView.tab("Meal"), width=400, height=100, font=my_font)
text_meal.pack(fill="both", expand=True)
text_meal.tag_config("center", justify="center")
text_meal.insert("end", "Hello world", "center") # 여기 Hello world 자리에 급식 넣기


#1교시부터 5교시 시작전까지는 meal.meal(0)을 사용하여 점심을, 5교시부터 야자 2교시까지는 meal.meal(1)을 사용하여 저녁을 보여줘야함

#날씨

#그날의 날씨에 맞는 흐림, 맑음, 비 같은 일러스트 필요 https://www.flaticon.com/search?word=weather&color=black&shape=outline 여기서 찾아보는것이 중요할듯



app.mainloop()
