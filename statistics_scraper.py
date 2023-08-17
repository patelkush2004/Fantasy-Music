import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

load_dotenv()

# the following code is to access the spotify API. We need to get a token to access the API.
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

token = get_token()

####################################################################################################################

num_artists = 500
url = "https://kworb.net/spotify/artists.html"
url2 = "https://www.billboard.com/charts/artist-100/" #billboard artist 100 - artist ranking
url3 = "https://www.billboard.com/charts/hot-100/" #billboard hot 100 - song ranking
url4 = "https://www.billboard.com/charts/billboard-200/" #billboard 200 - album ranking
artists = [] # list of artist names
artists_pictures = [] # list of artist pictures
daily_streams = [] # list of daily streams for each artist, award every day
total_streams = [] # list of total streams for each artist, award at end of week
billboard_hot_100_artists = [] # billboard hot 100. list of top daily artists. if you're artist is on this, you get points. award at end of week.
billboard_hot_100_artists_picture = [] # artist picture of the top 100 artist.
billboard_hot_100_song = [] # billboard hot 100. list of top daily songs. if you're artist is on this, you get points. award at end of week. 
billboard_hot_100_song_artist = [] # artist of the top 100 song. 
billboard_hot_100_song_artist_picture = [] # artist picture of the top 100 song.
billboard_hot_200_album = [] # billboard 200. list of top daily albums. if you're artist is on this, you get points. award at end of week.
billboard_hot_200_album_artist = [] # artist of the top 200 album.
billboard_hot_200_album_cover = [] # album cover of the top 200 album.

# the following code is for the top "num_artists" artists on spotify. We get the artist name and the number of
# daily streams

def scrape_top_artists(): 
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='addpos sortable')
        rows = table.find_all('tr')[1:]  # Skip the header row
                
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                artist_name = cols[0].get_text()
                artists.append(artist_name)
                
                daily_streams_value = cols[2].get_text()
                daily_streams.append(float(daily_streams_value.replace(',', '')))
                
                total_streams_value = cols[1].get_text()
                total_streams.append(float(total_streams_value.replace(',', '')))
                        
            if len(artists) >= num_artists:
                break

        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
        
#this is for billboard artist 100

def scrape_hot_artists():
    response = requests.get(url2)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('div', class_='chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max')
        rows = table.find_all('div', class_='o-chart-results-list-row-container') 

        if table:
            for row in rows:
                cols = row.find_all('h3', id='title-of-a-story')
                artist_names = cols[0].get_text().strip()
                billboard_hot_100_artists.append(artist_names)
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")

#this is for billboard hot 100
def scrape_hot_songs():
    response = requests.get(url3)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('div', class_='chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max')
        rows = table.find_all('div', class_='o-chart-results-list-row-container')
        
        if table:
            for row in rows:
                cols = row.find_all('h3', id='title-of-a-story')
                song = cols[0].get_text().strip()
                billboard_hot_100_song.append(song)
                
                cols2 = row.find('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')
                if cols2:
                    artist = cols2.get_text().strip()
                    if 'Featuring' in artist:
                        artist = artist.split('Featuring')[0].strip()
                    if '&' in artist:
                        artist = artist.split('&')[0].strip()
                    if ',' in artist:
                        artist = artist.split(',')[0].strip()
                    billboard_hot_100_song_artist.append(artist)
                
                cols2 = row.find('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')
                if cols2:
                    artist = cols2.get_text().strip()
                    if 'Featuring' in artist:
                        artist = artist.split('Featuring')[0].strip()
                    if '&' in artist:
                        artist = artist.split('&')[0].strip()
                    if ',' in artist:
                        artist = artist.split(',')[0].strip()
                    billboard_hot_100_song_artist.append(artist)

#this is for the billboard 200 albums ranking
def scrape_hot_albums():
    response = requests.get(url4)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('div', class_='chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max')
        rows = table.find_all('div', class_='o-chart-results-list-row-container')
        
        if table:
            for row in rows:
                cols = row.find_all('h3', id='title-of-a-story')
                album = cols[0].get_text().strip()
                billboard_hot_200_album.append(album)
                
                cols2 = row.find('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')
                if cols2:
                    artist = cols2.get_text().strip()
                    if 'Featuring' in artist:
                        artist = artist.split('Featuring')[0].strip()
                    if '&' in artist:
                        artist = artist.split('&')[0].strip()
                    if ',' in artist:
                        artist = artist.split(',')[0].strip()
                    billboard_hot_200_album_artist.append(artist)
                
                cols2 = row.find('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')
                if cols2:
                    artist = cols2.get_text().strip()
                    if 'Featuring' in artist:
                        artist = artist.split('Featuring')[0].strip()
                    if '&' in artist:
                        artist = artist.split('&')[0].strip()
                    if ',' in artist:
                        artist = artist.split(',')[0].strip()
                    billboard_hot_200_album_artist.append(artist)
                
                cols3 = row.find('img', class_='c-lazy-image__img lrv-u-background-color-grey-lightest lrv-u-width-100p lrv-u-display-block lrv-u-height-auto')
                image = cols3.get('data-lazy-src')
                billboard_hot_200_album_cover.append(image) 

####################################################################################################################
# the following code uses the spotify api to get the artist picture for each artist we have in our list

def search_for_artist(token, artist_name, array_pictures):
    url5 = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    
    query_url = url5 + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"][0]["images"][2]['url']
    if len(json_result) == 0:
        array_pictures.append('None')
    else:
        array_pictures.append(json_result)

####################################################################################################################

scrape_top_artists()
scrape_hot_artists()
scrape_hot_songs()
scrape_hot_albums()
        
for artist in artists:
    search_for_artist(token, artist, artists_pictures) 

for artist in billboard_hot_100_song_artist:
    search_for_artist(token, artist, billboard_hot_100_song_artist_picture) 
    
for artist in billboard_hot_100_artists:
    search_for_artist(token, artist, billboard_hot_100_artists_picture) 


####################################################################################################################

#for i in range (0, num_artists):
    #print(f"{i+1}. {artists[i]} - {total_streams[i]} - {daily_streams[i]} - {artists_pictures[i]}")

#for i in range (0, len(billboard_hot_100_song)):
    #print(f"{i+1}. {billboard_hot_100_song[i]} - {billboard_hot_100_song_artist[i]} - {billboard_hot_100_song_artist_picture[i]}")
    
#for i in range (0, len(billboard_hot_100_artists)):
    #print(f"{i+1}. {billboard_hot_100_artists[i]} - {billboard_hot_100_artists_picture[i]}")

#for i in range (0, len(billboard_hot_200_album)):
    #print(f"{i+1}. {billboard_hot_200_album[i]} - {billboard_hot_200_album_artist[i]} - {billboard_hot_200_album_cover[i]}")
    

