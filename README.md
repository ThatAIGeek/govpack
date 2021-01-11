# **govpack**

## Ukrainian open data pack

This package was created to ease and speed up access to the public data published by the Government of Ukraine on the https://data.gov.ua/ website.

At this moment govpack package provides a easy download of few medical datasets from the mentioned web-site, as well as auto creation of pandas variables from the sets.

#### Installation:

pip install govpack

#### Usage:

```python

def create_pandas(link=str(), from_api=True, limit=int(), header=int(), force_download=False)

```

Main module of the package create_var has a function called **def create_pandas()**. This function takes such arguments:
  * link=str() # While from_api=True (set True by default), you need to pass as an input string, that contains a link on a dataset API from data.gov.ua dataset. In case of setting from_api into False, you should pass here a direct link on a dataset file (csv or excel format) from data.gov.ua.

  * from_api=True # If True (set True by default) you need to pass a link on a dataset API from data.gov.ua dataset into the link parameter. In other case you need to use direct link on dataset file (csv or excel format) from data.gov.ua

  * limit=int() # Limit the quantity of links from API that will be proceed by govpack script

  * header=int() # You don't need to pass anything here, except the case you need to debug table structure (see use cases). Here could be passed an inter that will define the row of header in pandas.read_excel.

  * force_download=False # If True (set False by default) create_pandas() method will try to download all dataset files (from data.gov.ua) that were used to create pandas variables

Here is an explanation from a data.gov.ua how to get link of the dataset you need and combine it with API 'https://data.gov.ua/api/3/action/package_show?id=':
  * https://data.gov.ua/pages/aboutuser2?fbclid=IwAR2P3KN8P8JhZu8GUhHQZ4rh5-DlhSwp375kPFrbkwxprEvHm0mwhr2wQ1M

Also you could find several interesting dataset links beyond:
  * Інформація про погашені електронні рецепти за програмою реімбурсації лікарських засобів («Доступні ліки»): '5334586c-5bd1-4e24-9c14-9ba826cc9fa1'
  * Оплати надавачам медичної допомоги за програмою медичних гарантій: '25a46db9-2f15-4302-9b59-9bd761c80f46'
  * Оплати аптечним закладам за договорами реімбурсації лікарських засобів («Доступні ліки») з НСЗУ: '959dca0a-9b74-41ff-a7c8-f8de6398a219'
  * Відомості про транспортні засоби та їх власників: '06779371-308f-42d7-895e-5a39833375f0'

After installing **govpack** and opening Python in your terminal you could use this code example:

```python
from govpack.create_var import create_pandas
var1 = create_pandas('https://data.gov.ua/api/3/action/package_show?id=959dca0a-9b74-41ff-a7c8-f8de6398a219')
var1['dataset_0'].head()
```

You also could use a direct link from the data.gov.ua on a data file(in this case you will have only one key 'dataset_0'):

```python
link = 'https://data.gov.ua/dataset/1703061d-e0c4-4393-8a29-fc154d2705fe/resource/506977cc-1793-41ee-b14e-6d2bab7c02f4/download/pasport-naboru-danikh.xlsx'
var2 = govpack.create_pandas(link=link, from_api = False)
var2['dataset_0'].head()
```

Below are several use cases that you could follow with Colab notebooks:

  * Opening from API + a bit of visualisation: https://colab.research.google.com/drive/1GxJarOwAsfxSNVa71BCjBKFVHbax_JWq?usp=sharing

  * Opening from direct link on file, a bit of debugging and analysis: https://colab.research.google.com/drive/1GcSM2DHaQm9aabtiUen9BsjHd9Ytioi7?usp=sharing

  * Opening from zip files, ranking, clustering: https://colab.research.google.com/drive/1FxIOxPBy04rBWR2zqRcSzmfiJrqFNiFU?usp=sharing
