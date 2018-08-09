from edit_html import strip_email_and_link
from edit_html import strip_html_tags
from edit_html import strip_other_world
from edit_html import strip_script_tag
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def get_url(url):

    urllist = list()
    url = urlopen(url)
    chk_div = re.compile('^(section_headline|section_body)')
    chk_news=re.compile('read')

    bs = BeautifulSoup(url,"html.parser")

    for link in bs.find_all("div",{"class":chk_div}):
        for page in link.findAll("a",href=chk_news):
            if 'href' in page.attrs:
                urllist.append(page.attrs['href'])

    return urllist

def get_title_and_content(url):

    url = urlopen(url)
    bs = BeautifulSoup(url,"html.parser")
    news_content=''
    news_title=''

    for link in bs.find("h3",{"id":"articleTitle"}):
        news_title=strip_html_tags(link)

    for link in bs.find("div",{"id":"articleBodyContents"}):
        text = strip_other_world(link)
        text = strip_script_tag(link)
        text = strip_html_tags(text)
        news_content += text

    news_content = strip_email_and_link(news_content)
    return news_title,news_content



