#Importing packages that are used by the script
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

            #"url": "https://data.gov.ua/dataset/193cb9ba-e12e-4987-a9a9-d464e834593e/resource/7b345ccc-f1d7-42ea-b32c-b5e528793c79/download/reimbursement_released_prescriptions_2019.csv",
            #"qa": {"updated": "2020-07-14T10:48:15.623335", "openness_score": 3, "archival_timestamp": "2020-07-06T14:16:59.611608",
            #"format": "CSV", "openness_score_reason_args": "[[\"CSV\", 3]]",
            #"created": "2019-11-21T01:54:26.863847" <<<<<<<<<< use to filter a year in a big collections

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

        ### REPLACE WITH FUNCTIONS/CLASSES LATER ###

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
                                # globals()[output_name] = output_name_e
                                print('csv4')
                    elif ext == 'excel':
                        try:
                            globals()[output_name] = pd.read_excel(z.open(f_name), header=header)
                            print('excel1')
                        except ValueError as e:
                            urlretrieve(url, f_name)
                            print("Can't create pd dataset for: \"" + f_name + "\", because of the Error: \n\"" + str(e).rstrip() + "\"\nThe file has been downloaded for a manual parsing.")
                            # globals()[output_name] = output_name_e
                            print('excel2')
                    else:
                        urlretrieve(url, f_name)
                        # globals()[output_name] = output_name_e
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
