# *Note*: This uses the unreliable method of querying the spotify track name and artist on YouTube


def get_YT_equivalent_of_Spotify_playlist_tracks():
    import os
    import spotipy
    import subprocess as sp
    from youtubesearchpython import VideosSearch  # To query YT
    # To access authorised Spotify data
    from spotipy.oauth2 import SpotifyClientCredentials

    ###----Authenticating with Client API Key and Secrets----###
    try:
        client_id = os.environ['SPOT_CLIENT_ID']
        client_secret = os.environ['SPOT_CLIENT_SECRET']
    except Exception:
        print('Could not load spotify credentials from system environment variables')
        print('Exiting. . .')
        return None # Invalid URI

    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    # spotify object to access API
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    print('Connected to spotify')

    try:
        with open('spot_playlists.txt') as f:
            spot_playlist_uris = f.read().splitlines()

        spot_playlist_ids = []
        for spot_playlist_uri in spot_playlist_uris:
            spot_playlist_ids.append(
                spot_playlist_uri.split('?')[0].split('/')[-1]
            )

        spotify_playlist_songs = []
        for spot_playlist_id in spot_playlist_ids:
            # Iterate through spotify playlist tracks
            for i in sp.playlist(spot_playlist_id)['tracks']['items']:
                # Name of the song
                track_name = i['track']['name']
                # First 1 or 2 artist(s) that worked on the song
                track_artists = ' '.join([artist['name']
                                        for artist in i['track']['artists'][:2]])

                spotify_playlist_songs.append(f'{track_name} {track_artists}')

        spot_error = 0  # No errors encountered

    except Exception:
        spot_error = 1  # Error was encountered

    # if spot_error:
    #     ...

    YT_links = []
    for index, search_query in enumerate(spotify_playlist_songs):
        first_src_result = VideosSearch(search_query, limit=1).result()[
            'result'][0]['link']
        if not first_src_result in YT_links:
            YT_links.append(first_src_result)
            print(f'Loading: Track {index+1} of {len(spotify_playlist_songs)}')
        else:
            print(
                f'Removing duplicate: Track {index+1} of {len(spotify_playlist_songs)}')

    return YT_links

if __name__ == '__main__':
    get_YT_equivalent_of_Spotify_playlist_tracks()

