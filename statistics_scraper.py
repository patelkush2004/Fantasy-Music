import requests
from bs4 import BeautifulSoup

num_artists = 100
url = "https://kworb.net/spotify/artists.html"
url2 = "https://www.billboard.com/charts/artist-100/"
artists = []
daily_artists = []
daily_streams = []
top_daily_songs = []

# the following code is for the top "num_artists" artists on spotify. We get the artist name and the number of
# daily streams
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
                    
        if len(artists) >= num_artists:
            break

    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

response2 = requests.get(url2)
if response2.status_code == 200:
    soup = BeautifulSoup(response2.content, 'html.parser')
    table = soup.find('div', class_='chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max')
    rows = table.find_all('div', class_='o-chart-results-list-row-container') 

    if table:
        for row in rows:
            cols = row.find_all('h3', id='title-of-a-story')
            artist_names = cols[0].get_text()
            daily_artists.append(artist_names)
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")
    
#for idx, artist in enumerate(artists, start=1):
    #print(f"{idx}. {artist} - {daily_streams[idx-1]:,}")

print(daily_artists)
