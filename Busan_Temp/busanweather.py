from  bs4 import BeautifulSoup
from urllib import request

url = "http://www.weather.go.kr/weather/observation/currentweather.jsp"
cols = ["현재일기","시정","운량","중하운량","현재기온",
        "이슬점온도","불쾌지수","일강수","습도","풍향","풍속","해면기압"]

def get_city_temp(soup,city,tag="td"):
    return soup.find(tag, text=city).findNextSiblings()

def get_html(url=url):
    html = request.urlopen(url).read().decode('euc-kr')
    return BeautifulSoup(html, "html.parser")

def print_cols_data(city,temps,cols=cols):
    print('[*]{}'.format(city))
    for info,data in zip(cols,temps):
        print('[%s]%s\n'%(info,data.text))

if __name__=='__main__':
    soup = get_html(url)
    citylist = ["부산", "대구", "서울", "광주"]
    for city in citylist:
        temps = get_city_temp(soup=soup,city=city)
        print_cols_data(city=city,temps=temps)




