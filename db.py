from dotenv import load_dotenv
import os
import requests
import sqlite3
load_dotenv()

conn = sqlite3.connect('steam.sqlite')

STEAM_KEY=os.getenv('STEAM_KEY')
STEAM_ID=os.getenv('STEAM_ID')
getGamesURL = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&include_appinfo=1&include_played_free_games=1&format=json'.format(STEAM_KEY, STEAM_ID)

response = requests.get(getGamesURL)

if (response.status_code == 200):
    parsed = response.json()
    for game in parsed['response']['games']:
        games = game['name']
        appid = game['appid']
        time = game['playtime_forever']
        image = game['img_logo_url']

        image_url = "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/{}/{}.jpg".format(appid,image)
        timeType = 0

        if (time > 60):
            time = time%60
            # TimeType = 1 = Hours
            timeType = 1
        else:
            # TimeType = 0 = Minutes
            timeType = 0
        print("{}, {}, {}, {}, {}".format(games, appid, timeType, time, image_url))
        # Does the Game's name contain a quotation mark
        if ("'" in games):
            print(timeType)
            print(time)
            conn.execute('INSERT or IGNORE INTO Games (Name, AppID, TimeType, Time, Image) VALUES("{}",{},{},{},"{}")'.format(games, appid, timeType, time, image_url))
        else:
            print(timeType)
            print(time)
            conn.execute("INSERT or IGNORE INTO Games (Name, AppID, TimeType, Time, Image) VALUES('{}',{},{},{},'{}')".format(games, appid, timeType, time, image_url))
conn.commit()
print("Total changes: " + str(conn.total_changes))
conn.close()

# https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/{APPID}/{URL}.jpg