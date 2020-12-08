# govpack
## Ukrainian open data pack
This package was created to ease and speed up access to the public data published by the Government of Ukraine on the https://data.gov.ua/ website.

At this moment govpack package provides a easy download of few medical datasets from the mentioned web-site, as well as auto creation of pandas variables from the sets.

###
Prerequisites:
Python >= 3.6, pandas, xlrd

####
Installation:
pip install -i https://test.pypi.org/simple/ govpack-yarusx

#####
Usage example:
After installing govpack-yarusx (test version) and opening python in your terminal:

* Importing govpack:\
import govpack

* Importing med_apis - dictionary that contains dataset name and API link (from data.gov.ua) key-value pairs:\
from govpack.get_apis import med_apis

* Looking through the dictionary with APIs for different dataset collections:\
med_apis

* Creating a string with a link to the first (as example) dataset collection:\
api = list(med_apis.values())[0]

* Checking what we’ve got:\
api

* Importing get_urls and create_datasets functions:\
from govpack.get_data import get_urls, create_datasets

* Creating a dictionary that contains link to dataset file and its extension as a key-value pairs:\
urls = get_urls(api)

* Creating a dictionary that contains variable name (dataset_ + its No. according to urls dict) and pandas data frame as a key-value pairs. I.e.  dataset_0 will relate to 'https://data.gov.ua/dataset/193cb9ba-e12e-4987-a9a9-d464e834593e/resource/9fceb2ba-6fd3-42f8-8ffd-dd7d7c2ba821/download/opis-atributiv-naboru-danikh.xlsx‘. 'download = True‘ will cause downloading of the dataset files. Useful option while having troubles with creating datasets for some files with 'create_datasets’:\
datasets = create_datasets(urls, download = False)

* Checking heads and the first five rows in the dataset_0:\
datasets['dataset_0'].head()

You could also follow described above usecase from this picture:

![](https://github.com/ThatAIGeek/govpack/blob/develop/govpack_usecase.png)
