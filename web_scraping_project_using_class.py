import requests
import re
from bs4 import BeautifulSoup


class google_websites:
    def __init__(self, val):
        self.val = val

    def url_creator(self):
        page = requests.get(self.val)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def implementation(self, soup):
        num = 100
        k = 1
        my_list = []
        while (num != 0):
            for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):

                s = []
                s = re.split(":(?=http)", link["href"].replace("/url?q=", ""))
                st = s[0]
                x = st.partition('&sa')
                my_list.append(x[0])
                num = num - 1
                if (num == 0):
                    break
            if (num == 0):
                break
            elif (num != 0):
                k = int(k)
                k = k + 1
                k = str(k)
                url = f'https://www.google.com/search?q={search_query}/page' + k
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
        return my_list

    def printing(self, my_list):
        cnt = 1
        for itr in my_list:
            print(cnt)
            print(itr)
            cnt = cnt + 1


search_query = input("enter what you want to google: ")
url = f'https://www.google.com/search?q={search_query}'
my_obj = google_websites(val=url)
my_obj.url_creator()
my_obj.implementation(my_obj.url_creator())
my_obj.printing(my_obj.implementation(my_obj.url_creator()))

