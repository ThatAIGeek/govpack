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

```python
from govpack import *
modules = dir()
print(modules)
apis = get_apis.apis(med_apis.list)
apis
names = med_apis.names
names
pandas_var_dict1 = create_var.create_pandas(apis[0]) # this could take some time
pandas_var_dict1['dataset_1'].head()

#You also could use a direct link from the data.gov.ua on a data file(in this case you will have only one key 'dataset_0'):
pandas_var_dict2 = create_var.create_pandas('https://data.gov.ua/dataset/1703061d-e0c4-4393-8a29-fc154d2705fe/resource/506977cc-1793-41ee-b14e-6d2bab7c02f4/download/pasport-naboru-danikh.xlsx', from_api = False, force_download = False)
pandas_var_dict2['dataset_0'].head()
```

You could also follow a use case described above from this picture ('get_data' module name has been replaced by 'create_var', and 'create_pandas' method name simplified to 'pandas'):

![Use case](https://drive.google.com/uc?export=view&id=1bMJjPz2CqpVOwnZcdbP7X6YSUtAWiTiZ)

Or you could check one of the use cases in this Colab notebook here:

https://colab.research.google.com/drive/1GxJarOwAsfxSNVa71BCjBKFVHbax_JWq
