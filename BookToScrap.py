import threading           🥰🥰🥰🥰
import requests
import time
from bs4 import BeautifulSoup


def MultipleThreading():         ❤️❤️❤️❤️❤️
    star_time = time.time()

    def get_requests(i):
        list =[]
        url = f'https://quotes.toscrape.com/page/{i}/'
        html_text = requests.get(url).text
        #print(html_text)

        soup = BeautifulSoup(html_text, 'html.parser')

        qoutes = soup.findAll('div', {'class': "quote"})
        for i in qoutes:
            text = i.find('span', {'class': "text"})
            list.append(text)

        print(list)
    for i in range(10):
        get_requests(i)
        thread = threading.Thread(target=get_requests, args=(i, ))        😜😜😜
        thread.start()

        print(thread)
    endtime = time.time()

    print(endtime-star_time)


MultipleThreading()
                                😮😮😮😮😮