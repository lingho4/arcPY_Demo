from newsapi import NewsApiClient
from dataclasses import dataclass
from typing import List
import csv
import re
from datetime import datetime, timedelta


@dataclass
class oStruct:
    id: int
    names: List[str]
    count: int

# oblast definitions
obl1 = oStruct(id=1, names=['Cherkasy'], count=0)
obl2 = oStruct(id=2, names=['Chernihiv'], count=0)
obl3 = oStruct(id=3, names=['Chernivtsi'], count=0)
obl4 = oStruct(id=4, names=['Crimea'], count=0)
obl5 = oStruct(id=5, names=['Dniprop'], count=0)
obl6 = oStruct(id=6, names=['Donetsk'], count=0)
obl7 = oStruct(id=7, names=['Ivano-Frankivsk', 'Ivano'], count=0)
obl8 = oStruct(id=8, names=['Kharkiv'], count=0)
obl9 = oStruct(id=9, names=['Kherson'], count=0)
obl10 = oStruct(id=10, names=['Khmel'], count=0)
obl11 = oStruct(id=11, names=['Kyiv', 'Kiev'], count=0)
obl12 = oStruct(id=12, names=['Kiev'], count=0)
obl13 = oStruct(id=13, names=['Kirovohrad'], count=0)
obl14 = oStruct(id=14, names=['Lviv'], count=0)
obl15 = oStruct(id=15, names=['Luhans'], count=0)
obl16 = oStruct(id=16, names=['Mykolayiv'], count=0)
obl17 = oStruct(id=17, names=['Odessa', 'Odesa'], count=0)
obl18 = oStruct(id=18, names=['Poltava'], count=0)
obl19 = oStruct(id=19, names=['Rivne'], count=0)
obl20 = oStruct(id=20, names=['Sevastopol'], count=0)
obl21 = oStruct(id=21, names=['Sumy', 'Sumska'], count=0)
obl22 = oStruct(id=22, names=['Ternopil'], count=0)
obl23 = oStruct(id=23, names=['Transcarpathia'], count=0)
obl24 = oStruct(id=24, names=['Vinnytsya'], count=0)
obl25 = oStruct(id=25, names=['Volyn'], count=0)
obl26 = oStruct(id=26, names=['Zaporizhzhya'], count=0)
obl27 = oStruct(id=27, names=['Zhytomyr'], count=0)

# create the array containing all oblast objects
oblastArray = [obl1, obl2, obl3, obl4, obl5, obl6, obl7, obl8, obl9, obl10, obl11, obl12, obl13, obl14, obl15, obl16, obl17, obl18, obl19, obl20, obl21, obl22, obl23, obl24, obl25, obl26, obl27]


def count_oblast_mentions(text, oblast_list):
    text = text.lower()  
    for oblast in oblast_list:
        for name in oblast.names:
            if re.search(r'\b' + re.escape(name.lower()) + r'\b', text):
                oblast.count = oblast.count + 1


def retrieveData():
    # Initialize NewsApiClient with API key
    newsapi = NewsApiClient(api_key='xxxxxxxxxxxxxxxxxxxxxx')


    # get yesterdays date and the day before that for the date range
    yesterday = datetime.today() - timedelta(days=1)
    previousDay = datetime.today() - timedelta(days=2)
    # get them as strings
    yesterdayStr = yesterday.strftime('%Y-%m-%d')
    previousDayStr = previousDay.strftime('%Y-%m-%d')

    # Fetch news articles for the specified date range
    topArticles = newsapi.get_everything(q='Ukraine War', language='en', from_param=previousDayStr, to=yesterdayStr)

    for article in topArticles['articles']:
        if 'content' in article and article['content']:
            count_oblast_mentions(article['content'], oblastArray)
        elif 'description' in article and article['description']:
            count_oblast_mentions(article['description'], oblastArray)

    # Define CSV output file path
    csv_file = 'headlineData.csv'

    # Write the results to a CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['ID_1', 'Mentions'])
        # Write oblast mention counts
        for oblast in oblastArray:
            writer.writerow([oblast.id, oblast.count])

    print("News data recorded")