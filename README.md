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
After installing govpack-yarusx (test version) please use (both from command line or in your python file): <b>"from med_pkg import get_data"</b>. This will cause the downloading of 3 datasets and 1 data description files from https://data.gov.ua/dataset/959dca0a-9b74-41ff-a7c8-f8de6398a219.

Installation and usage example:

![alt text](https://github.com/ThatAIGeek/govpack/blob/develop/govpack_usecase.png?raw=true)

###### Alpha release action plan:
- [ ]  possible package use cases:
  - usecase 1
  - usecase 2
  - usecase 3
- [ ]  get list of datasets to focus on at first stage
  - dataset1 link
  - dataset2 link
  - dataset3 link
- [ ]  write a simple package to setup and push into pypi
- [ ]  decide on the best format for datasets(scipy?)
- [ ]  add first dataset for the package
- [ ]  create usage examples
