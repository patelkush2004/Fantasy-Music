import requests
from bs4 import BeautifulSoup

num_artists = 500
url = "https://kworb.net/spotify/artists.html"
url2 = "https://www.billboard.com/charts/artist-100/" #billboard artist 100 - artist ranking
url3 = "https://www.billboard.com/charts/hot-100/" #billboard hot 100 - song ranking
url4 = "https://www.billboard.com/charts/billboard-200/" #billboard 200 - album ranking
url5 = "https://chartmasters.org/most-streamed-artists-ever-on-spotify/" #to link picture to artist name
page = 1
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

fake_artist_names = []
fake_artist_pictures = []

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
            
            total_streams_value = cols[1].get_text()
            total_streams.append(float(total_streams_value.replace(',', '')))
                    
        if len(artists) >= num_artists:
            break

    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")
        
# the following code is to link the artist name to their picture. 
response = requests.get(url5)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', id='table_1')
    rows = table.find_all('tr')
    
    for row in rows:
        name = row.find('b')
        if name:
            fake_artist_names.append(name.get_text())
        
        image = row.find('img')
        if image:
            fake_artist_pictures.append(image.get('src'))

print(len(fake_artist_names))
        
            
        
        
#this is for billboard artist 100
response = requests.get(url2)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('div', class_='chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max')
    rows = table.find_all('div', class_='o-chart-results-list-row-container') 

    if table:
        for row in rows:
            cols = row.find_all('h3', id='title-of-a-story')
            cols2 = row.find('img', class_='c-lazy-image__img lrv-u-background-color-grey-lightest lrv-u-width-100p lrv-u-display-block lrv-u-height-auto')
            artist_names = cols[0].get_text().strip()
            artist_pictures = cols2.get('data-lazy-src')
            billboard_hot_100_artists.append(artist_names)
            billboard_hot_100_artists_picture.append(artist_pictures)
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

#this is for billboard hot 100
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
                billboard_hot_100_song_artist.append(artist)
            
            cols2 = row.find('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')
            if cols2:
                artist = cols2.get_text().strip()
                billboard_hot_100_song_artist.append(artist)
                
            cols3 = row.find('img', class_='c-lazy-image__img lrv-u-background-color-grey-lightest lrv-u-width-100p lrv-u-display-block lrv-u-height-auto')
            image = cols3.get('data-lazy-src')
            billboard_hot_100_song_artist_picture.append(image)

#this is for the billboard 200 albums ranking
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
                billboard_hot_200_album_artist.append(artist)
            
            cols2 = row.find('span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')
            if cols2:
                artist = cols2.get_text().strip()
                billboard_hot_200_album_artist.append(artist)
                
            
            cols3 = row.find('img', class_='c-lazy-image__img lrv-u-background-color-grey-lightest lrv-u-width-100p lrv-u-display-block lrv-u-height-auto')
            image = cols3.get('data-lazy-src')
            
            billboard_hot_200_album_cover.append(image) 
    
#for i in range (0, num_artists):
    #print(f"{i+1}. {artists[i]} - {total_streams[i]} - {daily_streams[i]}")

#for i in range (0, len(billboard_hot_100_song)):
    #print(f"{i+1}. {billboard_hot_100_song[i]} - {billboard_hot_100_song_artist[i]} - {billboard_hot_100_song_artist_picture[i]}")
    
#for i in range (0, len(billboard_hot_100_artists)):
    #print(f"{i+1}. {billboard_hot_100_artists[i]} - {billboard_hot_100_artists_picture[i]}")

#for i in range (0, len(billboard_hot_200_album)):
    #print(f"{i+1}. {billboard_hot_200_album[i]} - {billboard_hot_200_album_artist[i]} - {billboard_hot_200_album_cover[i]}")
    

