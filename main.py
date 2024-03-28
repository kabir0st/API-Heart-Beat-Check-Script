import json
from datetime import datetime

import pytz
import requests

# Define Nepali time zone
nepal_timezone = pytz.timezone('Asia/Kathmandu')

# Get current time in Nepali time zone
current_time_nepal = datetime.now(nepal_timezone)

# Format the time string
formatted_time = current_time_nepal.strftime('%Y-%m-%d %H:%M:%S')

WEBHOOK_URL = ""

COLORS = {
    "BooksMandala": 0x0a67a0,
    "Phoenix BooksMandala": 0x0a67a0,
    "GweiStation Web": 0xa9cee9,
    "GweiStation API": 0xa9cee9,
    "DegenHouse": 0x03fca1,
    "DegenHouse API": 0x03fca1
}


def send_to_discord(servers):

    embed = {"title": f"{formatted_time}", "color": 0x008000, "fields": []}
    mention = False
    for server in servers.keys():
        res = ""
        status = check_server_status(servers[server])
        if status:
            res = "🟢 Online"
        else:
            mention = True
            res = "🔴 Offline"
        embed["fields"].append({
            "name": f"{res} : {server} ",
            "value": "",
            "inline": False,
            "color": COLORS[server]
        })
    payload = {"embeds": [embed]}
    if mention:
        payload["content"] = "@here"
        payload['embeds'][0]['color'] = 0xFF0000
    headers = {"Content-Type": "application/json"}

    res = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    print(res.text, res.status_code)


def check_server_status(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        if response.status_code in [401, 200]:
            return True
        return False
    except requests.ConnectionError:
        return False


def main():
    servers = {
        "BooksMandala": "https://booksmandala.com",
        "Phoenix BooksMandala": "admin/login",
        "GweiStation Web": "https://gweistation.io/",
        "GweiStation API": "/api/users/whoami/",
        "DegenHouse": "https://degenhouse.xyz/",
        "DegenHouse API": "/api/users/whoami/",
    }
    send_to_discord(servers)


if __name__ == "__main__":
    main()
