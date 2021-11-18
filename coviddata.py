import requests
import time
from playsound import playsound
pincode= input('Enter Pincode:')
date= input('Enter Date:')
URL ='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}'.format(pincode,date)
header={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

def avaliability():
    count=0
    result= requests.get(URL,headers=header)
    answer=result.json()
    data=answer['centers']
    for centers in data:
        for sessions in centers['sessions']:
            if((sessions["min_age_limit"]==18) & (sessions["available_capacity"]>0)):
                count=1
                print("Avaliable")
                print(centers["name"])
                print(sessions["date"])
                print(sessions["vaccine"])
                print(sessions["available_capacity"])
                print(sessions["slots"])
    
    if(count == 1):
        playsound('mixkit-positive-notification-951.wav')
        return True
    if(count == 0):
        print("Not Available")
        return False

while(avaliability() != True):
    time.sleep(2)
    avaliability()