#Importing packages that are used by the script
import json
from urllib.request import urlopen, urlretrieve
import re
import time
import pandas as pd

#Getting links from API
def get_urls(api_link):
    try:
        with urlopen(api_link) as response:
            source = response.read()
    except ValueError as e:
        print("Unable to open "+str(api_link)+"due to "+str(e))
        return
    #Loading data from the API link as an python object with JSON
    data = json.loads(source)
    #Making a dict with key - dataset file url-link, and value - file extension (xls/xlsx or csv)
    urls = dict()
    for item in data['result']['resources']:
        url = item['url']
        f_name = re.findall('download/([\w\-\.]+)', url)[0]
        ext = f_name.rsplit('.')[1]
        if ext == 'csv':
            extension = 'csv'
        elif ext == 'xlsx' or ext == 'xls':
            extension = 'excel'
        else:
            extension = None
        urls.update({url : extension})

    return urls

def create_datasets(urls, download = False):
    datasets_list = list()
    datasets = dict()

    for iteration, (url, extension) in enumerate(urls.items()):
        datasets_list.append("dataset_" + str(iteration))
        f_name = re.findall('download/([\w\-\.]+)', url)[0]
        #Creating pandas datasets
        try:
            if extension == 'csv':
                globals()["dataset_" + str(iteration)] = pd.read_csv(url)
            elif extension == 'excel':
                globals()["dataset_" + str(iteration)] = pd.read_excel(url)
        except ValueError as e:
                globals()["dataset_" + str(iteration)] = "Got an Error while creating pd dataset for " + str(f_name) + ". Please download and parse this file manually."
                print("Can not create pd dataset for: \"" + f_name + "\", because of the Error: \n\"" + str(e).rstrip() + "\"\nPlease download to download and parse this file manually.")
        datasets.update({datasets_list[iteration] : globals()["dataset_" + str(iteration)]})

        if download == True:
            urlretrieve(url, f_name)

    return datasets
