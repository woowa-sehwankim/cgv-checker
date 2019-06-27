import requests 
from enum import Enum
from bs4 import BeautifulSoup

class Theater: 
    YOUNGSAN = '0013' 

class ScreenType: 
    IMAX = '018'


def getStartTimesForMovie(name, date): 
    url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx' 
    params = {
        'areacode': '01',
        'date': date,  
        'theatercode': Theater.YOUNGSAN, 
        'screencodes': ScreenType.IMAX
    }

    response = requests.get(url, data=params) 
    html = response.text

    soup = BeautifulSoup(html, 'html.parser') 
    movieTimeTableList = soup.select('.col-times')


    targetTimeTable = [timeTable.select('.info-timetable').find_all('a') for timeTable in movieTimeTableList if name in timeTable.get_text()] 
    return targetTimeTable

print(getStartTimesForMovie('스파이더맨', '20190701'))
 