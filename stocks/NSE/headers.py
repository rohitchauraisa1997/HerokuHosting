import time
from pprint import pprint
import json
import requests
from bs4 import BeautifulSoup

def get_headers():
    stock_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=PIIND"
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

    response = requests.get(stock_url, headers=headers)
    # print(response)
    # print(response.status_code)
    # print(response.text) 

    soup = BeautifulSoup(response.text, "html.parser")
    # time.sleep(5)
    data_array = soup.find(id="responseDiv")
    # print(type(data_array))
    data_array = data_array.getText().strip()
    # print("*"*40)
    # print(type(data_array))
    # print(data_array)
    data_array = json.loads(data_array)
    print(type(data_array))
    pprint(data_array['data'][0].keys())
    return data_array['data'][0].keys()
# headers = get_headers()

# for header in headers:
#     print(header)