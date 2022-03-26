import requests
import time
from datetime import datetime
from pytz import timezone

tz = timezone('EST')
previous_day = None

def check_in():
    print("Initiating check-in...")
    headers = {
        'Host': 'app.campusclear.com',
        'Accept': 'application/json',
        'X-Timezone': 'America/New_York',
        'Accept-Language': 'en-us',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/json',
        'Origin': 'https://app.campusclear.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Referer': '---------',
    }

    data = '----------'
    try:
        response = requests.post('https://app.campusclear.com/api/covid/update-health-log', headers=headers, data=data)
        status_code = response.status_code
        response_json = response.json()
        loggedAt = response_json["logAt"]
        print(f"Check-in successful!\nStatus code: {status_code}\nLogged at {loggedAt}")
    except:
        print("Error occurred, please add traceback u silly goose.")

while True:
    date = datetime.now(tz)
    day = date.day
    if day != previous_day:
        check_in()
    else:
        print("Waiting...")
    previous_day = day
    time.sleep(7200)


