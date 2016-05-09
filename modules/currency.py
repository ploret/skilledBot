import urllib.request
from bs4 import BeautifulSoup


def get_html_source_code(url):
    """ get html code by provided url """
    request = urllib.request.urlopen(url)
    return request.read()


def get_usd(html):
    """ parse usd exchange rate in html code """
    soup = BeautifulSoup(html, "html.parser")
    soup.select('table.local_table tr td big')
    usd_list = []
    for big_tag in soup.find_all('big')[0:2]:
        usd_list.append(float(big_tag.text))

    usd_info = {
        'buy': usd_list[0],
        'sale': usd_list[1]
    }

    return usd_info
