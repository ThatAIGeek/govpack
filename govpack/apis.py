from enum import Enum

api = 'https://data.gov.ua/api/3/action/package_show?id='

med_dict = {'Інформація про погашені електронні рецепти за програмою реімбурсації лікарських засобів («Доступні ліки»)':'5334586c-5bd1-4e24-9c14-9ba826cc9fa1',
            'Оплати надавачам медичної допомоги за програмою медичних гарантій':'25a46db9-2f15-4302-9b59-9bd761c80f46',
            'Оплати аптечним закладам за договорами реімбурсації лікарських засобів («Доступні ліки») з НСЗУ':'959dca0a-9b74-41ff-a7c8-f8de6398a219'
            }

class Med_apis(Enum):
    med_api0 = api+list(med_dict.values())[0]
    med_api1 = api+list(med_dict.values())[1]
    med_api2 = api+list(med_dict.values())[2]
