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
names = get_apis.apis(med_apis.names)
names
pandas_var_list = get_data.create_pandas(apis[0]) # that will take some time
pandas_var_list
```

You could also follow described above use case from this picture:

![Use case](https://github.com/ThatAIGeek/govpack/blob/develop/use_case.png)
