from bs4 import BeautifulSoup
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date=input("Which year you want to travel to? Type the date in this format YYYY-MM-DD: ")
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

URL= "https://www.billboard.com/charts/hot-100/" + date
response=requests.get(URL,headers=headers)

soup=BeautifulSoup(response.text,'html.parser')
song_title=soup.select(selector="li ul li h3")
song_names=[i.getText().strip() for i in song_title]

CLIENT_ID = "Your_client_ID"
CLIENT_SECRET = "Your_client_secret"

REDIRECT_URI = "https://example.org/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username="Ayush373"))

user_id = sp.current_user()['id']
results = sp.current_user() # this is the full dictionary. Now you can pick out your user_id

formatted_results = json.dumps(results, indent=4) # this creates a formatted view of the JSON
with open("results.json", mode="w") as file:
    file.write(formatted_results) # useful if you want to see what the function returned, and in a nice format

user_id = results["id"] # query the dictionary for the "id"
print(user_id)
song_uris=[]
year=date.split('-')[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except (IndexError, KeyError):
        print(f"{song} doesn't exist in Spotify. Skipped.")

print('song urls added')

playlist = sp.user_playlist_create(
    user=user_id,
      name=f'{date} Billboard 100', 
      public=False,
      collaborative=False,
      description="100 top songs")
print("playlist created")

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)

print(f"\nThe playlist has been created. A total of {len(song_uris)}/100 of the top 100 songs were found! ")
