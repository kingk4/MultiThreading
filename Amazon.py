import threading
import requests
import time
from bs4 import BeautifulSoup
                                🤞😒👌😍
headers= {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'session-id=131-1078585-7101164; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PK"; ubid-main=132-4167795-0386741; session-token=bbcqkV4Jd3FH9JFgk97whQ1y8M9AjIJ65VwupUeUPXFx8uoXuIYDc3mZxFy5C2R24tRnjocQWX/+txroJIBi8frG1KZAkSy4Br9IkViqnEHnGH964KaVkGFvzFTeUF6bfRoTVo+QNrhvSxFNKrQyZHluRDKDRzf6c3KaaXr4DfHt5vPPJ8AVc/1uz35y6joG; csm-hit=tb:77H98J0DVYQTTF0NYF16+sa-77H98J0DVYQTTF0NYF16-0D4CZG3K9DWPRRZ7Q4A7|1647008351886&t:1647008351886&adb:adblk_no',
'downlink': '1.05',
'ect': '3g',
'rtt': '400',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}


def MultipleThreading():           ❤️❤️❤️
    star_time = time.time()            # star the timing of execution  👍😜

    def get_requests(i):

        link_list =[]
        url = f'https://www.amazon.com/s?k=macbook+air+laptop&page={i}&crid=282GNWGPCNSBL&qid=1647007505&sprefix=macbook+air+laptopa%2Caps%2C407&ref=sr_pg_{i}'
        html_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_text, 'html.parser')
        items = soup.findAll('h2', {'class':'a-size-mini'})
        for data in items:
            link = data.find('a')['href']
            # print(link)
            link_list.append("https://www.amazon.com"+link)
        #print(link_list)

        def followLinks(links):
            html_text_1 = requests.get(links, headers=headers).text
            soup1 = BeautifulSoup(html_text_1, 'html.parser')
            product_name = soup1.find('span', {'id': "productTitle"}).text
            print(product_name)


        for links in link_list:
            thread_1 = threading.Thread(target=followLinks, args=(links, ))              # create inner thread
            thread_1.start()                           # staring inner thread         🚛🚜🚛


    for i in range(1):
        thread = threading.Thread(target=get_requests, args=(i, ))                    # main  thread
        thread.start()                     # main thread starting

        print(thread)
    endtime = time.time()                  # ending execution time
    time.sleep(2)
    print(endtime-star_time)

MultipleThreading()                    # calling main  threading  funtion
                                    🤨🤨😥😥😮❤️