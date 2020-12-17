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
Usage:

```python

def create_pandas(link=str(), from_api=True, header=int(), force_download=False)

```

Main module of the package create_var has a function called **def create_pandas()**. This function takes such arguments:
  * link=str() # While from_api=True (set True by default), you need to pass as an input string, that contains a link on a dataset API from data.gov.ua dataset. In case of setting from_api into False, you should pass here a direct link on a dataset file (csv or excel format) from data.gov.ua.

  * from_api=True # If True (set True by default) you need to pass a link on a dataset API from data.gov.ua dataset into the link parameter. In other case you need to use direct link on dataset file (csv or excel format) from data.gov.ua\

  * header=int() # You don't need to pass anything here, except the case you need to debug table structure (see use cases). Here could be passed an inter that will define the row of header in pandas.read_excel.

  * force_download=False # If True (set False by default) create_pandas() method will try to download all dataset files (from data.gov.ua) that were used to create pandas variables

After installing govpack-yarusx (test version) and opening python in your terminal:

```python
import govpack
var1 = govpack.create_pandas(govpack.med_api0)
var1['dataset_1'].head()

#You also could use a direct link from the data.gov.ua on a data file(in this case you will have only one key 'dataset_0'):

link = 'https://data.gov.ua/dataset/1703061d-e0c4-4393-8a29-fc154d2705fe/resource/506977cc-1793-41ee-b14e-6d2bab7c02f4/download/pasport-naboru-danikh.xlsx'
var2 = govpack.create_pandas(link=link, from_api = False)
var2['dataset_0'].head()

```

You could also follow a use case described above from this picture:

![Use case](https://drive.google.com/uc?export=view&id=1wVmBgAs6kFkMtOqppFgM_a4bIuD8ReYP)

Or you could check one of the use cases in this Colab notebook:

https://colab.research.google.com/drive/1GxJarOwAsfxSNVa71BCjBKFVHbax_JWq
