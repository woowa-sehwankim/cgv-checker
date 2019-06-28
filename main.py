import requests
import re
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

    def findRemainingSeats(aTag):
        p = re.compile('\d+석')
        return p.search(aTag).group()

    def extractMovieTimeAndSeats(timeTable):
        aTagList = timeTable.find(class_='info-timetable').find_all('a')
        return [(aTag.attrs['data-playstarttime'], aTag.attrs['data-playendtime'], findRemainingSeats(aTag.get_text())) for aTag in aTagList]

    targetTimeTable = [extractMovieTimeAndSeats(
        timeTable) for timeTable in movieTimeTableList if name in timeTable.get_text()]
    return targetTimeTable


print(getStartTimesForMovie('스파이더맨', '20190701'))
