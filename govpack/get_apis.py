def apis(apis_list):
    basic_api = 'https://data.gov.ua/api/3/action/package_show?id='
    apis = list()
    for api in apis_list:
        apis.append(basic_api+api)

    return apis
