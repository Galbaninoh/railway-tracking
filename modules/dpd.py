
import datetime
from cloudscraper import CloudScraper

s= CloudScraper()

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Opera\";v=\"112\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "TCPID=1245519474594829464; TC_PRIVACY=0%40007%7C2%7C2%7C224%7C114%7C5380%401%2C2%2C3%40%401714758430157%2C1714758430157%2C1730310430157%40_v8AAAAAAAAAAAD-CgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA_Co%3D; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.2096568244.1714758442; _ga=GA1.1.439500797.1714758442; _ga_Q3RB6RNZ25=GS1.1.1714765247.2.0.1714765247.60.0.0; _ga_1K56TRMV25=GS1.1.1714765247.2.0.1714765247.0.0.0; ntrack=s%3A5hYTOYmM7F5_fzmbhuQufCg36tdBCmbO.sX4vva%2BETB5B92SiCZUbrkSMa%2FcB1WY4LLCJYEM1Lto",
    "Referer": "https://tracking.dpd.de/status/en_US/404",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

username = "s3bdolst8u8krc7-country-it"
password = "xkjvhet7fs68iq2"
proxy = "rp.proxyscrape.com:6060"
proxy_auth = "{}:{}@{}".format(username, password, proxy)
proxies = {
    "http":"http://{}".format(proxy_auth)
}

def convert_to_unix_timestamp(date_string):
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
    timestamp = int(date_obj.timestamp())
    return timestamp

def track(tracking:str):
    r = s.get("https://tracking.dpd.de/rest/plc/en_US/" + tracking, headers=headers, proxies=proxies)
    try:
        updates = r.json()["parcellifecycleResponse"]["parcelLifeCycleData"]["scanInfo"]["scan"]
        result = []
        for update in updates:
            time = convert_to_unix_timestamp(update["date"])
            description = update["scanDescription"]["content"][0]
            courierName = "DPD"
            location = update["scanData"]["location"]
            result.append({
                "courier" : courierName,
                "status" : description,
                "date" : time,
                "location" : location
            })
        return result
    except:
        return []
    
    