from pprint import pprint
import json 
import time
import subprocess
import os
import requests
from bs4 import BeautifulSoup
import sqlite3


from headers import get_headers

check = True
st_time = time.time()
i = 21
print(os.listdir(os.getcwd()))

if "data.db" in os.listdir(os.getcwd()):
    os.system("rm -rf data.db")
    os.system("python create_table.py")
while check:
    # if time.time() - st_time > 100:
    if time.time() - st_time > 100:
        print("exiting")
        check = False
    stockcode = "PIIND"
    stocks_list = ["PIIND","TCS"]
    stocks_list = ["PIIND"]
    
    for stockcode in stocks_list:
        stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+str(stockcode)
        print(stock_url)
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}

        response = requests.get(stock_url, headers=headers)
        # print(response)
        # print(response.status_code)
        # print(response.text) 

        soup = BeautifulSoup(response.text, "html.parser")
        time.sleep(5)
        data_array = soup.find(id="responseDiv")
        # print(type(data_array))
        data_array = data_array.getText().strip()
        # print("*"*40)
        # print(type(data_array))
        # print(data_array)
        data_array = json.loads(data_array)
        print(type(data_array))
        pprint(data_array)
        # print("*"*40)
        # pprint(data_array["data"][0]["averagePrice"])
        # # pprint(data_array["data"][0]["basePrice"])
        
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        headers_retreived = get_headers()
        length = (len(headers_retreived))
        # number_of_questions = "?, "*(length+1)
        number_of_questions = "?, "*68 + "?"
        
        print(number_of_questions)
        insert_query = "INSERT INTO stocks VALUES ({})".format(number_of_questions)
        print(insert_query)
        print("+"*100)
        print(list(data_array["data"][0].values()))
        print("+"*100)
        enter_list = list(data_array["data"][0].values())
        enter_list.insert(0,i)
        print("ENTERLIST")
        print(enter_list)
        print(tuple(enter_list))
        cursor.execute(insert_query,tuple(enter_list))
        connection.commit()
        
        if float(data_array["data"][0]["lastPrice"].replace(',','')) - float(data_array["data"][0]["previousClose"].replace(',','')) > 50:
            print("change is greater than 50")
            # sending_email()
            
        i+=1