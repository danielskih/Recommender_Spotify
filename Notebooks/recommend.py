import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.client_id, client_secret=config.client_secret))
def recommend(song):
    song_id = sp.search(song)['tracks']['items'][0]['id']
    result = sp.recommendations(seed_tracks=[song_id], limit=10, market='US')
    found = result['tracks'][0]['id']
    return 'Try and click that link: \nhttps://open.spotify.com/track/{} \nsee if you like it.'.format(found)