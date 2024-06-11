import requests
from deep_translator import GoogleTranslator
import datetime

translator = GoogleTranslator(source='auto', target='en')

def convert_to_unix_timestamp(date_string):
    date_format = "%Y-%m-%d %H:%M:%S"
    date_obj = datetime.datetime.strptime(date_string, date_format)
    timestamp = int(date_obj.timestamp())
    return timestamp

def track(tracking_code):
    API_URL = "http://www.gti568.com:8082/selectTrack.htm?documentCode=" + tracking_code

    headers = {
        "Accept" :"application/json, text/javascript, */* q=0.01",
        "Accept-Encoding" : "gzip, deflate",
        "Origin" :"http://www.gti56.com",
        "Referrer" : "http://www.gti56.com"
    }

    r = requests.get(API_URL, headers = headers)
    response = r.json()
    if r.status_code == 200:
        if response[0]["ack"] == "true":
            tracking_updates = response[0]["data"][0]["trackDetails"]
            result = []
            for update in tracking_updates:
                description = translator.translate(update["track_content"] + update["track_location"])
                courierName = "GTI"
                date = update["track_createdate"]
                location = update["track_city"]
                result.append({
                    "courier" : courierName,
                    "status" : description,
                    "date" : convert_to_unix_timestamp(date),
                    "location" :  location
                })
            print(result)
            return result
        else:
            return []
    else:
        return []
