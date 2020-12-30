import json
from urllib.request import urlopen, urlretrieve
import re
import time
import pandas as pd
import zipfile
from io import BytesIO

#Getting links from API
def create_pandas(link=str(), from_api=True, limit=int(), header=int(), force_download=False):

    #Creating a dict of dataset files links and extensions
    urls = dict()

    def get_extentstion(url):
        f_name = re.findall('download/([\w\-\.]+)', url)[0]
        ext = f_name.rsplit('.')[1]
        if ext == 'csv':
            extension = 'csv'
        elif ext == 'xlsx' or ext == 'xls':
            extension = 'excel'
        elif ext == 'zip':
            extension = 'zip'
        else:
            extension = 'not_supported'
        return extension

    if from_api == True:
        try:
            with urlopen(link) as response:
                source = response.read()
        except ValueError as e:
            print("Unable to open "+str(link)+"due to "+str(e))
            return
        #Loading data from the API link as an python object with JSON
        data = json.loads(source)
        for item in data['result']['resources']:
            url = item['url']
            extension = get_extentstion(url)
            urls.update({url : extension})
    else:
        url = link
        f_name = re.findall('([\w\-\.]+)', url)[0]
        extension = get_extentstion(url)
        urls.update({url : extension})

    datasets_list = list()
    datasets = dict()

    for iteration, (url, extension) in enumerate(urls.items()):
        if iteration >= limit and limit != int() : break
        output_name = "dataset_" + str(iteration)
        datasets_list.append(output_name)
        f_name = re.findall('download/([\w\-\.]+)', url)[0]
        output_name_e = "Got an Error while creating pd dataset for " + str(f_name) + ". The file has been downloaded for a manual parsing."

        #Creating pandas datasets
        if extension == 'zip':
            r = urlopen(url)
            with zipfile.ZipFile(BytesIO(r.read())) as z:
                for f_name in z.namelist():
                    ext = f_name.rsplit('.')[1]
                    if ext == 'csv':
                        try:
                            globals()[output_name] = pd.read_csv(z.open(f_name), sep=',')
                        except:
                            try:
                                globals()[output_name] = pd.read_csv(z.open(f_name), sep=';')
                            except ValueError as e:
                                urlretrieve(url, f_name)
                                print("Can't create pd dataset for: \"" + f_name + "\", because of the Error: \n\"" + str(e).rstrip() + "\"\nThe file has been downloaded for a manual parsing.")
                                print('csv4')
                    elif ext == 'excel':
                        try:
                            globals()[output_name] = pd.read_excel(z.open(f_name), header=header)
                            print('excel1')
                        except ValueError as e:
                            urlretrieve(url, f_name)
                            print("Can't create pd dataset for: \"" + f_name + "\", because of the Error: \n\"" + str(e).rstrip() + "\"\nThe file has been downloaded for a manual parsing.")
                            print('excel2')
                    else:
                        urlretrieve(url, f_name)
                        print('else1')

        elif extension == 'csv':
            try:
                globals()[output_name] = pd.read_csv(url, sep=',')
            except:
                try:
                    globals()[output_name] = pd.read_csv(url, sep=';')
                except ValueError as e:
                    urlretrieve(url, f_name)
                    print("Can't create pd dataset for: \"" + f_name + "\", because of the Error: \n\"" + str(e).rstrip() + "\"\nThe file has been downloaded for a manual parsing.")
                    globals()[output_name] = output_name_e

        elif extension == 'excel':
            try:
                globals()[output_name] = pd.read_excel(url, header=header)
            except ValueError as e:
                urlretrieve(url, f_name)
                print("Can't create pd dataset for: \"" + f_name + "\", because of the Error: \n\"" + str(e).rstrip() + "\"\nThe file has been downloaded for a manual parsing.")
                globals()[output_name] = output_name_e
        else:
            urlretrieve(url, f_name)
            globals()[output_name] = output_name_e

        try:
            datasets.update({datasets_list[iteration] : globals()[output_name]})
        except:
            print('Can not update datasets dictionary with Key: ' +str(datasets_list[iteration]))

        if force_download == True:
            urlretrieve(url, f_name)

    return datasets
