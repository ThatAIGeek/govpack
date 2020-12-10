#Importing packages that are used by the script
import json
from urllib.request import urlopen, urlretrieve
import re
import time
import pandas as pd

#Getting links from API
def create_pandas(api_link, force_download = False):
    try:
        with urlopen(api_link) as response:
            source = response.read()
    except ValueError as e:
        print("Unable to open "+str(api_link)+"due to "+str(e))
        return
    #Loading data from the API link as an python object with JSON
    data = json.loads(source)
    #Creating a list of dataset files links
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
            extension = 'not_supported'
        urls.update({url : extension})

    def err(e):
        return ("Can't create pd dataset for: \"" + f_name + "\", because of the Error: \n\"" + str(e).rstrip() + "\"\nThe file has been downloaded for a manual parsing.")

    datasets_list = list()
    datasets = dict()

    for iteration, (url, extension) in enumerate(urls.items()):
        output_name = "dataset_" + str(iteration)
        datasets_list.append(output_name)
        f_name = re.findall('download/([\w\-\.]+)', url)[0]
        output_name_e = "Got an Error while creating pd dataset for " + str(f_name) + ". The file has been downloaded for a manual parsing."
        #Creating pandas datasets
        if extension == 'csv':
            try:
                globals()[output_name] = pd.read_csv(url, sep=',')
            except:
                try:
                    globals()[output_name] = pd.read_csv(url, sep=';')
                except ValueError as e:
                    urlretrieve(url, f_name)
                    print(err(e))
                    globals()[output_name] = output_name_e

        elif extension == 'excel':
            try:
                globals()[output_name] = pd.read_excel(url)
            except:
                urlretrieve(url, f_name)
                print(err(e))
                globals()[output_name] = output_name_e

        datasets.update({datasets_list[iteration] : globals()[output_name]})

        if force_download == True:
            urlretrieve(url, f_name)

    return datasets
