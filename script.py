
import requests
import os
import time

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

zipcode = "846009"
date = "14-05-2021"
center_id = 698532
age = 18

retry = 1
while(retry < 10000000000):

    slot = 0
    center_name = ""
    response = requests.get(('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin'), headers=headers, params={
                    'pincode': zipcode,
                    'date': date,
                })
    if response.status_code == 200:
        json_data = response.json()['centers']
        for center in json_data:
            ses = center['sessions'][0]
            if ses["available_capacity"] > 0 and ses["min_age_limit"] > age:
                print(ses["available_capacity"])
                print(center["name"])
                slot += 1
                center_name += center["name"]

    if slot > 0:
        notify("Vaccin slot available", center_name)
        time.sleep(10)
    else:
        retry += 1
        time.sleep(60)





    