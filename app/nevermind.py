import spotipy
import spotipy as spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id="74be65a15ded404ea3859bf31f5aa9bf",
                                               client_secret="b74ace61acb64f4e9d383d1501491481",
                                               redirect_uri="https://google.com",
                                               scope='user-read-playback-state,user-modify-playback-state'))
float
# Shows playing devices
res = sp.devices()
pprint(res)

# Change track
sp.start_playback(uris=['spotify:track:0HUTL8i4y4MiGCPId7M7wb'])