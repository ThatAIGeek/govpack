# govpack
## Ukrainian open data pack
This package was created to ease and speed up access to the public data published by the Government of Ukraine on the https://data.gov.ua/ website.

At this moment govpack package provides a easy and fast download of datasets from this source:
Official data name: "Оплати аптечним закладам за договорами реімбурсації лікарських засобів («Доступні ліки») з НСЗУ", time period: 2019-2020 years, source link: https://data.gov.ua/dataset/959dca0a-9b74-41ff-a7c8-f8de6398a219

<!-- First dataset (meds_set1). Official data name: "Інформація про погашені електронні рецепти за програмою реімбурсації лікарських засобів («Доступні ліки»)", time period: 2018-2020 years, source link: https://data.gov.ua/dataset/5334586c-5bd1-4e24-9c14-9ba826cc9fa1

Third dataset (meds_set1). Official data name: "Оплати надавачам медичної допомоги за програмою медичних гарантій", time period: 2019-2020 years, source link: https://data.gov.ua/dataset/25a46db9-2f15-4302-9b59-9bd761c80f46 -->

###
Installation:
pip install -i https://test.pypi.org/simple/ govpack-yarusx

####
Usage:
After installing govpack-yarusx (test version) please use (both from command line or in your python file): <b>"from med_pkg import get_data"</b>. This will cause the downloading of 3 datasets and 1 data description files from https://data.gov.ua/dataset/959dca0a-9b74-41ff-a7c8-f8de6398a219.

Installation and usage example:

![alt text](https://github.com/ThatAIGeek/govpack/blob/develop/govpack_usecase.png?raw=true)

##### Alpha release action plan:
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
