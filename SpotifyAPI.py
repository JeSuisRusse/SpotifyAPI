import sys, os
import spotipy
import spotipy.util as util
os.system('clear')
song_train_id = []
x_train=[]
y_train=[]
x_test=[]
y_test=[]
username = "21fpmnq7rdbpn6nsjsoxrc6lq"
clientId = "080ec5426f3b47678789e27613642e9f"
clientSecret = "866a4d2d91864f8395f1c34117e32063"
redirectURI = "http://localhost/"
scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private streaming ugc-image-upload user-follow-read user-library-modify user-read-private user-read-birthdate user-read-email user-top-read user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played'
token = util.prompt_for_user_token(username,scope,client_id=clientId,client_secret=clientSecret, redirect_uri='http://localhost/')
sp = spotipy.Spotify(auth=token)
if token:
	os.system('clear')
	print('██████╗ ██╗   ██╗███████╗███████╗███████╗ █████╗ ██████╗ ██╗')
	print('██╔══██╗██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██║')
	print('██████╔╝██║   ██║███████╗███████╗█████╗  ███████║██████╔╝██║')
	print('██╔══██╗██║   ██║╚════██║╚════██║██╔══╝  ██╔══██║██╔═══╝ ██║')
	print('██║  ██║╚██████╔╝███████║███████║███████╗██║  ██║██║     ██║')
	print('╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝')                                                    
	print("What is the token of the playlist you want to list songs (and other informations)")
	results = sp.user_playlist_tracks(user = username, playlist_id=input('[*]>>'), fields=None, limit=100, offset=0, market=None)
	for item in results['items']:
		track = item['track']
		song_train_id.append(sp.audio_features(tracks = [track['id']]))
		tab = sp.audio_features(tracks = [track['id']])
		print(track['name'] + ' | by ' + track['artists'][0]['name'] + ' | id = ' + track['id'] + ' | duration (in ms) = ' + str(track['duration_ms']) + ' | tempo = ' + str(tab[0]['valence']))
for songs in song_train_id:
	x_train.append([songs[0]["id"]])