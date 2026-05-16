CONST_CITIES = [
  {"rank":1,  "name":"New York, NY",          "temp":55.0},
  {"rank":2,  "name":"Los Angeles, CA",        "temp":66.0},
  {"rank":3,  "name":"Chicago, IL",            "temp":50.0},
  {"rank":4,  "name":"Houston, TX",            "temp":70.0},
  {"rank":5,  "name":"Phoenix, AZ",            "temp":75.0},
  {"rank":6,  "name":"Philadelphia, PA",       "temp":55.5},
  {"rank":7,  "name":"San Antonio, TX",        "temp":70.0},
  {"rank":8,  "name":"San Diego, CA",          "temp":63.0},
  {"rank":9,  "name":"Dallas, TX",             "temp":67.0},
  {"rank":10, "name":"Jacksonville, FL",       "temp":69.0},
  {"rank":11, "name":"Austin, TX",             "temp":69.0},
  {"rank":12, "name":"San Jose, CA",           "temp":60.0},
  {"rank":13, "name":"Fort Worth, TX",         "temp":66.0},
  {"rank":14, "name":"Columbus, OH",           "temp":52.0},
  {"rank":15, "name":"Charlotte, NC",          "temp":60.0},
  {"rank":16, "name":"Indianapolis, IN",       "temp":52.0},
  {"rank":17, "name":"San Francisco, CA",      "temp":57.0},
  {"rank":18, "name":"Seattle, WA",            "temp":52.0},
  {"rank":19, "name":"Denver, CO",             "temp":50.0},
  {"rank":20, "name":"Nashville, TN",          "temp":60.0},
  {"rank":21, "name":"Oklahoma City, OK",      "temp":62.0},
  {"rank":22, "name":"El Paso, TX",            "temp":64.0},
  {"rank":23, "name":"Washington, DC",         "temp":58.0},
  {"rank":24, "name":"Louisville, KY",         "temp":57.0},
  {"rank":25, "name":"Las Vegas, NV",          "temp":67.0},
  {"rank":26, "name":"Memphis, TN",            "temp":63.0},
  {"rank":27, "name":"Portland, OR",           "temp":54.0},
  {"rank":28, "name":"Baltimore, MD",          "temp":57.0},
  {"rank":29, "name":"Milwaukee, WI",          "temp":46.0},
  {"rank":30, "name":"Albuquerque, NM",        "temp":56.0},
  {"rank":31, "name":"Tucson, AZ",             "temp":69.0},
  {"rank":32, "name":"Fresno, CA",             "temp":63.0},
  {"rank":33, "name":"Sacramento, CA",         "temp":61.0},
  {"rank":34, "name":"Mesa, AZ",               "temp":75.0},
  {"rank":35, "name":"Kansas City, MO",        "temp":56.0},
  {"rank":36, "name":"Atlanta, GA",            "temp":63.0},
  {"rank":37, "name":"Omaha, NE",              "temp":51.0},
  {"rank":38, "name":"Colorado Springs, CO",   "temp":47.0},
  {"rank":39, "name":"Raleigh, NC",            "temp":60.0},
  {"rank":40, "name":"Long Beach, CA",         "temp":65.0},
  {"rank":41, "name":"Virginia Beach, VA",     "temp":60.0},
  {"rank":42, "name":"Minneapolis, MN",        "temp":45.0},
  {"rank":43, "name":"Tampa, FL",              "temp":72.0},
  {"rank":44, "name":"New Orleans, LA",        "temp":70.0},
  {"rank":45, "name":"Arlington, TX",          "temp":67.0},
  {"rank":46, "name":"Wichita, KS",            "temp":57.0},
  {"rank":47, "name":"Bakersfield, CA",        "temp":65.0},
  {"rank":48, "name":"Aurora, CO",             "temp":50.0},
  {"rank":49, "name":"Miami, FL",              "temp":77.0},
  {"rank":50, "name":"Cleveland, OH",          "temp":50.0},
]

def get_cities_ftemp(lst: list[dict[str, int]]) -> dict[str, float] :
    return { city['name']: city['temp'] for city in lst }

dict_c_f = get_cities_ftemp(CONST_CITIES)
print(dict_c_f)

def get_cities_ctemp(d: dict[str, float]) -> dict[str, float]:
    return { k: round((v-32)*5/9, 2) for k,v in d.items() }

dict_c_c = get_cities_ctemp(dict_c_f)
print(dict_c_c)

def dict_f_to_c(dict_of_temps):
    return {key: (value-32)/1.8
            for key, value in dict_of_temps.items()}

dict_c_c_l = dict_f_to_c(dict_c_f)
print(dict_c_c_l)