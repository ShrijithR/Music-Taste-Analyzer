import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from creds import client_id, client_secret
import pandas as pd


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret, 
    redirect_uri="http://127.0.0.1:9090", 
    username="Shrijith R",
    scope=scope))

limit = 20
offset = 0

def api_call():
    return sp.current_user_saved_tracks(limit=limit)

results = api_call()


def get_details(results):
    details = []
    item_list = list(results.items())
    # total_songs = results['total']
    for i in range(0,limit):
        artist_name = item_list[1][1][i]['track']['name']
        song_name= item_list[1][1][i]['track']['album']['artists'][0]['name']
        details.append({'artist': artist_name, 'song': song_name})
        # artist_dict[artist_name]['album'] = item_list[1][1][i]['track']['album']['name']
    return details
details_list = get_details(results)
# print(details)

def create_dataset(details_list):
    # df = pd.read_csv('datasets/details.csv')
    # df = pd.DataFrame(columns=['song', 'artist'])
    # list_for_df = [[i['song'], i['artist']] for i in details_list]
    # print(list_for_df)
    # df.append(list_for_df)
    # print(df)
    df = pd.DataFrame(details_list)
    df.to_csv("details.csv")
    # print("done")
create_dataset(details_list)
# def update_dataset():
#     pd.read_csv("datasets\song_list.csv")
#     pass

# with open("saved_tracks_2.py", "w") as file:
#     file.write(str(results))
