import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing  import  StandardScaler
import numpy as np
import json
from spotipy.oauth2 import SpotifyClientCredentials
import config
import spotipy

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.client_id, client_secret=config.client_secret))
with open('../Data/genres_top50s_tracks.json') as json_file:
    data = json.load(json_file)

# flatten the data
data_flat = [data[i] for i in data.keys()]

from itertools import chain
data_flat=chain(*data_flat[:])

data_flat = list(data_flat)
with open('../Data/song_ids.txt') as file:
    data_2 = [i.replace('\n','') for i in file]
data = data_flat + data_2

n=0

  

with open('../data/genres_audio_feats.json', 'w') as f:
    for i in data:
        feats = sp.audio_features(tracks=i)
        print(feats)
        json.dump(feats, f)



