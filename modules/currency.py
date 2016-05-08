import urllib.request
from bs4 import BeautifulSoup



def get_html_source_code(url):
    request = urllib.request.urlopen(url)
    return request.read()

def get_privatbank_usd(html):
    soup = BeautifulSoup(html, "html.parser")
    usdDigits = soup.select('table.local_table tr td big')
    usdList = []
    for big_tag in soup.find_all('big')[0:2]:
        usdList.append(float(big_tag.text))

    usdDict = {
        'buy': usdList[0],
        'sale': usdList[1]
    }

    return usdDict
