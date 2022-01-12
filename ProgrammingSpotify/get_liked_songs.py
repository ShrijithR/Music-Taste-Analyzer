import pickle
from typing import ItemsView
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

def get_data_spotify(limit, offset):
    item_list = []
    while True:
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        results_list = list(results.items())
        item_list += results_list[1][1]
        total_songs = results['total']
        # total_songs = 6
        offset += limit
        # songs_collected = offset+limit
        if offset>total_songs:
            break
        
    return item_list, total_songs

def extract_and_add(item_list, songs_collected):
    details = []
    for i in range(0,songs_collected):
        artist_name = item_list[i]['track']['name']
        song_name= item_list[i]['track']['album']['artists'][0]['name']
        details.append({'artist': artist_name, 'song': song_name})
        # artist_dict[artist_name]['album'] = item_list[1][1][i]['track']['album']['name']
    
    return details

def create_dataset(details_list):
    df = pd.DataFrame(details_list)
    df.to_csv("details.csv")

limit = 20
offset = 0

item_list, songs_collected = get_data_spotify(limit, offset)
details_list = extract_and_add(item_list, songs_collected)
create_dataset(details_list)
