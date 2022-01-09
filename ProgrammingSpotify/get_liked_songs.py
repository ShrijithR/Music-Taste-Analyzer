import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

import pandas as pd

client_id=""
client_secret=""
scope = "user-library-read"
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
#     client_id="06469cd4845b4cc2b61a61463f0c4f2d",
#     client_secret="6954c723f16d4d29915f0f535fb100b0",
# ))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="",
    client_secret="", 
    redirect_uri="http://127.0.0.1:9090", 
    username="Shrijith R",
    scope=scope))

# def show_tracks(results):
#     for item in results['items']:
#         track = item['track']
#         print("%32.32s %s" % (track['artists'][0]['name'], track['name']))

limit = 20
offset = 0

def api_call():
    return sp.current_user_saved_tracks(limit=2)

results = api_call()

def get_details(results, limit, offset, total):
    item_list = list(results.items())
    total_songs = results['total']
    for i in range(0,2):
        print(item_list[1][1][i]['track']['name'])
        print(item_list[1][1][i]['track']['album']['artists'][0]['name'])
        print(item_list[1][1][i]['track']['album']['name'])

def update_dataset():
    pd.read_csv("datasets\song_list.csv")
    pass

# with open("saved_tracks_2.py", "w") as file:
#     file.write(str(results))
