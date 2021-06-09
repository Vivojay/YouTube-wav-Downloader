from bs4 import BeautifulSoup
import requests
import urllib.request

"""
list of user agents

Chrome Browser User Agents
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36
Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36
"""

#user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
url = "https://music.youtube.com/playlist?list=PLJoxe5lD4jPOxa-ntt4rr4SqGjda2n5FL"

def read_webpage(url):
    headers={'User-Agent':user_agent,}

    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need

    data = data.decode('utf-8-sig')
    souped_data = BeautifulSoup(data, "html.parser")

    return (data, souped_data)

pagecontents = read_webpage(url)[1]

from ytmusicapi import YTMusic

def getPlaylistInfo(playlistURL):
    ytmusic = YTMusic()
    if '&' in playlistURL:
        playlistID = playlistURL.lstrip('https://music.youtube.com/playlist?list=')[:playlistURL.lstrip('https://music.youtube.com/playlist?list=').find('&')]
    else:
        playlistID = playlistURL.lstrip('https://music.youtube.com/playlist?list=')

    YTPlaylistTitle = ytmusic.get_playlist(playlistId=playlistID)['title']
    YTPlaylistAuthor = ytmusic.get_playlist(playlistId=playlistID)['author']['name']
    YTVidTrackUrls = ['https://www.youtube.com/watch?v='+i['videoId'] for i in ytmusic.get_playlist(playlistId=playlistID)['tracks']]
    YTVidTrackTitles = [i['title'] for i in ytmusic.get_playlist(playlistId=playlistID)['tracks']]
    return [list(zip(YTVidTrackUrls, YTVidTrackTitles)), f'Playlist "{YTPlaylistTitle}" by "{YTPlaylistAuthor}"']

if __name__ == '__main__':
    import json
    a=getPlaylistInfo(url)
    print(json.dumps(a, indent=4))
