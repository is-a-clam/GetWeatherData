import requests
import json
import csv

weather_filepath = '/Users/wlam/Desktop/Isaac/Coding/Python/weather.json'
weather_file = open(weather_filepath, "r")
weather_file.close()

URL = "https://data.weather.gov.hk/weatherAPI/opendata/opendata.php"

data_csv = [['', '', '', ''],
            ['', 'Year', 'Month', 'Average Temperature']]

for year in range(1947, 2020):
    PARAMS = {'dataType':'CLMTEMP', 'rformat':'json', 'station':'HKO', 'year':str(year)}
    r = requests.get(url = URL, params = PARAMS)
    data_string = r.json()
    data = json.loads(json.dumps(data_string))
    temps = data["data"]
    curr_month_total = 0
    prev_month = 1
    prev_day = 1
    for day_temp in temps:
        month = int(day_temp[1])
        day = int(day_temp[2])
        temp = float(day_temp[3])
        if prev_month != month:
            data_csv.append(['', str(year), str(prev_month), str(float(curr_month_total) / float(prev_day))])
            curr_month_total = temp
        else:
            curr_month_total += temp
        prev_day = day
        prev_month = month
    data_csv.append(['', str(year), str(prev_month), str(float(curr_month_total) / float(prev_day))])

with open("weather.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data_csv)
