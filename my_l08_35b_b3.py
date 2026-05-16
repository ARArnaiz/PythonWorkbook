import my_l08_35b_b2 as ddd
import copy

book_dict = ddd.tuple_to_dict(ddd.authors_lst_to_tuple(ddd.CONST_BOOKS))
# print(book_dict)

CONST_CURRENCY_DATA = [
  {"rank":1,  "flag":"🇰🇼", "name":"Kuwaiti Dinar",         "code":"KWD", "usdPer":0.3069,    "perUsd":3.259,    "region":"ME"},
  {"rank":2,  "flag":"🇧🇭", "name":"Bahraini Dinar",         "code":"BHD", "usdPer":0.3760,    "perUsd":2.660,    "region":"ME"},
  {"rank":3,  "flag":"🇴🇲", "name":"Omani Rial",             "code":"OMR", "usdPer":0.3845,    "perUsd":2.601,    "region":"ME"},
  {"rank":4,  "flag":"🇯🇴", "name":"Jordanian Dinar",        "code":"JOD", "usdPer":0.7090,    "perUsd":1.410,    "region":"ME"},
  {"rank":5,  "flag":"🇬🇧", "name":"British Pound",          "code":"GBP", "usdPer":0.7502,    "perUsd":1.333,    "region":"EU"},
  {"rank":6,  "flag":"🇨🇭", "name":"Swiss Franc",            "code":"CHF", "usdPer":0.7874,    "perUsd":1.270,    "region":"EU"},
  {"rank":7,  "flag":"🇪🇺", "name":"Euro",                   "code":"EUR", "usdPer":0.8602,    "perUsd":1.162,    "region":"EU"},
  {"rank":8,  "flag":"🇺🇸", "name":"US Dollar",              "code":"USD", "usdPer":1.0000,    "perUsd":1.000,    "region":"AM"},
  {"rank":9,  "flag":"🇸🇬", "name":"Singapore Dollar",       "code":"SGD", "usdPer":1.2804,    "perUsd":0.7810,   "region":"AS"},
  {"rank":10, "flag":"🇨🇦", "name":"Canadian Dollar",        "code":"CAD", "usdPer":1.3752,    "perUsd":0.7272,   "region":"AM"},
  {"rank":11, "flag":"🇦🇺", "name":"Australian Dollar",      "code":"AUD", "usdPer":1.3988,    "perUsd":0.7149,   "region":"OC"},
  {"rank":12, "flag":"🇨🇳", "name":"Chinese Yuan",           "code":"CNY", "usdPer":6.8080,    "perUsd":0.1469,   "region":"AS"},
  {"rank":13, "flag":"🇸🇦", "name":"Saudi Riyal",            "code":"SAR", "usdPer":3.7500,    "perUsd":0.2667,   "region":"ME"},
  {"rank":14, "flag":"🇦🇪", "name":"UAE Dirham",             "code":"AED", "usdPer":3.6725,    "perUsd":0.2723,   "region":"ME"},
  {"rank":15, "flag":"🇯🇵", "name":"Japanese Yen",           "code":"JPY", "usdPer":158.666,   "perUsd":0.006303, "region":"AS"},
  {"rank":16, "flag":"🇰🇷", "name":"South Korean Won",       "code":"KRW", "usdPer":1376.0,    "perUsd":0.000727, "region":"AS"},
  {"rank":17, "flag":"🇮🇳", "name":"Indian Rupee",           "code":"INR", "usdPer":96.072,    "perUsd":0.01041,  "region":"AS"},
  {"rank":18, "flag":"🇧🇷", "name":"Brazilian Real",         "code":"BRL", "usdPer":5.0226,    "perUsd":0.1991,   "region":"AM"},
  {"rank":19, "flag":"🇲🇽", "name":"Mexican Peso",           "code":"MXN", "usdPer":19.45,     "perUsd":0.05141,  "region":"AM"},
  {"rank":20, "flag":"🇿🇦", "name":"South African Rand",     "code":"ZAR", "usdPer":18.12,     "perUsd":0.05519,  "region":"AS"},
]

def cur_to_dict(lst: list[dict]) -> dict[str, float]:
    return { item['code']: item['usdPer'] for item in lst }

curr_dict = cur_to_dict(CONST_CURRENCY_DATA)
# print(curr_dict)

def get_dict_in_curr(dt: dict[str, dict], dc: dict[str, float], curr: str = "USD") -> dict[str, dict]:
    return { k : { 'author first name' : v['author first name'],
                   'author last name' : v['author last name'],
                   'price' : round(v['price'] * dc[curr], 2) }
                    for k, v in dt.items() }

print(get_dict_in_curr(book_dict, curr_dict, "JPY"))

def get_dict_in_curr_c(dt: dict[str, dict], dc: dict[str, float], curr: str = "USD") -> dict[str, dict]:
    return {
        k: {**v, 'price': round(v['price'] * dc[curr], 2)}
        for k, v in dt.items()
    }

print(get_dict_in_curr_c(book_dict, curr_dict, "JPY"))

def get_dict_in_curr_c_alt(dt, dc, curr="USD"):
    result = copy.deepcopy(dt)
    for v in result.values():
        v['price'] = round(v['price'] * dc[curr], 2)
    return result

print(get_dict_in_curr_c_alt(book_dict, curr_dict, "JPY"))

def currency_conversion(books, new_currency):
    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price * conversions[new_currency]}
            for name, title, price in books}