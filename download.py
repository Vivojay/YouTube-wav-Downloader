from __future__ import unicode_literals 
from bs4 import BeautifulSoup
from bs4.element import TemplateString
from youtubesearchpython import VideosSearch
from tabulate import tabulate
from to_wav import convert_to_wav

import youtube_dl, sys, os
import requests
import subprocess as sp
import ffmpeg
import webbrowser as wb

curDir = os.path.split(__file__)[0]
os.chdir(curDir)

NAs = 0
skipDl = False

def my_hook(d):
    if d['status'] == 'downloading':
        print("Downloading: "+ str(round(float(d['downloaded_bytes'])/float(d['total_bytes'])*100,1))+"%", end = '\r')

def SET(x):
    return sorted(set(x), key=x.index)

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def notice():
    print('\n*Note: All same named files WILL BE OVERWRITTEN!\n')

def yt_srch():
    global skipDl
    res_cnt = 30
    srchtrm = ' '.join(sys.argv[2:])

    try:
        vidsObj = VideosSearch(srchtrm)
    except Exception:
        print('No search term, exiting...')
        os._exit(0)

    vids = vidsObj.result().get('result')
    vidinfos = [[i.get('link'), i.get('title')] for i in vids]
    vidtitles = [i[1] for i in vidinfos]

    while not len(vidtitles) >= res_cnt:
        prevLen = len(vidtitles)

        # vidsObj.next()
        # vids = vidsObj.result().get('result')
        # vidinfos.extend([[i.get('link'), i.get('title')] for i in vids])
        # vidtitles.extend(i[1] for i in vidinfos)
        
        try:
            vidsObj.next()
            vids = vidsObj.result().get('result')
            vidinfos.extend([[i.get('link'), i.get('title')] for i in vids])
            vidtitles.extend(i[1] for i in vidinfos)

        except Exception:
            # print('Less than 30 results')
            pass
        
        if len(vidinfos) <= prevLen:
            break

    if len(vidtitles)/2 < 30:
        print('Less than 30 results')
    
    # print(vidtitles)

    if len(vidtitles) != 0:
        vidinfos = vidinfos[:res_cnt]
        vidurls = [i[0] for i in vidinfos]
        vidtitles = [i[1] for i in vidinfos]
        ResultTable = tabulate([[i+1, vidtitles[i]] for i in range(0, len(vidtitles))], headers=['#', 'Results for '+srchtrm], tablefmt='pretty', stralign='left', colalign=['left', 'left'])
        print(ResultTable)

        UrlTable = tabulate([[i+1, vidurls[i]] for i in range(0, len(vidurls))], headers=['#', 'urls'], tablefmt='pretty', stralign='left', colalign=['left', 'left'])

        numsGet = input('Select #(s) [separated by spaces], (leave empty to skip): ')
        if numsGet == '':
            print('Skipping download')
            skipDl = True
        try:
            numsGet = [int(i) for i in numsGet.split()]
            urlsGet = [vidurls[i-1] for i in numsGet]
            return (urlsGet)
        except Exception:
            print('Atleast 1 invalid value entered...')
            os._exit(0)
            return False

    else:
        print('No results match your search')
        os._exit(0)

if not len(sys.argv) == 1:
    if sys.argv[1] == 's':
        urls = SET(yt_srch())
        if not skipDl and type(urls) in [list, set]:
            for i in urls:
                print('\t'+i)
        if urls is not None and not type(urls) == bool:
            urls = list(set(urls))
        else:
            # print('No results for', urls)
            os._exit(0)
    else:
        if sys.argv[-1] == 'urls':
            try:
                with open('urls.txt') as f:
                    contt = f.read()
            except Exception:
                raise
                print('Could not find "urls.txt" in folder, please retry')
                print('Exiting. . .')
                os._exit(0)

            notice()
            
            urls = contt.splitlines()
            urls = list(set(urls))

        if sys.argv[-1] == 'yt':
            try:
                with open('yt_playlist.txt', encoding="utf8", errors='ignore') as f:
                    contt = f.read().splitlines()
            except Exception:
                print('Could not find "yt_playlist.txt" in folder, please retry')
                print('Exiting. . .')
                os._exit(0)

            notice()
            
            import scrapeYTMusic as syt
            # All YT Music Playlists
            urls = []
            for playlistURL in contt:
                print(playlistURL)
                playlistInfo = syt.getPlaylistInfo(playlistURL)
                print(f'{playlistInfo[-1]}')
                urls_in_playlists = [i[0] for i in playlistInfo[0]]
                urls_in_playlists = list(set(urls_in_playlists))
                urls.extend(urls_in_playlists)

            # First YT Music Playlist Only

            # playlistURL = contt[0] # If you enter more than one playlists, we'll only consider the first one
            # playlistInfo = syt.getPlaylistInfo(playlistURL)
            # print(f'{playlistInfo[-1]}')
            # urls = [i[0] for i in playlistInfo[0]]
            # urls = list(set(urls))

            # urls = contt.split()

        if not len(sys.argv) == 1 and not sys.argv[-1] in ['urls', 'yt']:
            urls = [i for i in sys.argv[2:]]
            urls = list(set(urls))
            notice()
else:
    print('Error: No parameters entered, exiting...')
    os._exit(0)

#Default destination folder - Calculated via the "get_download_path()" function

dpath = get_download_path() #Default Path
# print(dpath)

try:
    if not sys.argv[1] == 's':
        path = sys.argv[1]
    
    else:
        path = '' #FILL THIS LATER
    
    # print(not skipDl)
    if (not os.path.exists(path) or path.isspace() or path == '') and not skipDl:
        if sys.argv[-1] not in ['urls', 'yt'] and not sys.argv[1] == 's':
            urls = [i for i in sys.argv[1:]]
            urls = list(set(urls))
            print(len(urls), 'video distinct urls entered')
            print('Invalid dest path: "', path, '"', sep = '')
            print('Path must be within double quotes and entered as the \'FIRST\' argument ONLY')
        path = input('\nYou can enter\n\t1) Absolute path to any destination folder \n\t\tor \n\t2) Just press return to download in default \'Downloads dir\'\nEnter here:: ')

        if path == '' or path.isspace():
            path = dpath
            print('Defaulting to downloads folder: "', get_download_path(), '"', sep = '')
        elif not os.path.exists(path):
            print('\t> Invalid destination path')
        else:
            pass

    while not os.path.exists(path) and not skipDl and path != dpath:
           
        path = input('Enter destination path: ')
        
        if path == '' or path.isspace() and not skipDl:
            path = dpath
        elif not os.path.exists(path) and not skipDl:
            print('\t> Invalid destination path:')
    else:
        if not skipDl:
            print(len(urls), 'video urls entered')
        if len(urls) == 0:
            print('Exiting...')
            os._exit(0)
except Exception:
    if not skipDl:
        print('Unknown destination path error')

Dpath = path

def vidinfo(URL):
    global NAs
    try:
        url = 'https://www.youtube.com/oembed?url=' + URL + '&format=json'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        vid_title = eval(str(s)).get('title')
        # vid_thumbnail = eval(str(s)).get('thumbnail_url')
        return vid_title
    except Exception:
        NAs += 1
        return 'N/A'

def vidthumb(URL):
    global NAs
    try:
        url = 'https://www.youtube.com/oembed?url=' + URL + '&format=json'
        r = requests.get(url).text
        vid_thumbnail = eval(r)['thumbnail_url']
        return vid_thumbnail
    except Exception:
        # NAs += 1
        return 'N/A'

try:
    #Main Download parameter: ydl_opts
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mka',

        # 'postprocessors': [{
        # 'key': 'FFmpegExtractAudio',
        # 'preferredcodec': 'mp3',
        # 'preferredquality': '192',
        #     }],

        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
        }],

        'outtmpl': path+'/%(title)s.mka', # Name the file as the title of the video in original mka format ...
                                          # [This will later be converted to wav]
        'noplaylist': True,
        'prefer_ffmpeg': True,
        'nocheckcertificate': True,
        'quiet': True,
        'progress_hooks': [my_hook],
        'no_warnings': True
    }

except Exception:
    print('Error encountered while setting download parameters, exiting')
    os._exit(0)

if skipDl:
    os._exit(0)

##--
print('\nLoading video data...')
# print(urls)
titles = [[i+1, vidinfo(urls[i]), urls[i]] for i in range(0, len(SET(urls)))]
titles = [list(i) for i in set([tuple(i) for i in titles])]
s = [i[1] for i in titles]
files = os.listdir(path)
duplicates = []

if len(set(s)) == 1 and s[0] == 'N/A' and not skipDl:
    print('Error: None of the entered urls is valid, exiting...')
    os._exit(0)

print('\nTHE FILES WILL BE SAVED IN:', path)
print('\nAudios from following URLs will get downloaded:\n')

titles = sorted(titles, key=lambda x: x[0])
print(tabulate(titles, tablefmt='pretty', headers = ('#', 'Video Name', 'URL')))

for i in s:
    if i+'.wav' in files:
        duplicates.append(i)
    elif i+'.mp3' in files:
        duplicates.append(i)
    elif i+'.mka' in files:
        duplicates.append(i)

if any(duplicates):
    print()
    print('-'*70)
    print('Duplicate files warning [These files will be skipped] (', len(duplicates), '):', sep='')
    print('-'*70)
    print(tabulate([[i] for i in duplicates], tablefmt='pretty', headers = ['Duplicates Files('+str(len(duplicates))+')'], colalign=('left',)))

download = input('\nConfirm download(s) (y/n)? ')

# Measure for URL shortening
titles = [
            i[:-1]+[
                    i[-1].replace('https://youtu.be/', 'https://www.youtube.com/watch?v=')
                ]
            if i[-1].startswith('https://youtu.be/')
            else i
            for i in titles
    ]

# Measure against duplicates
titles = [i for i in titles if not i[1] in duplicates]

urls = [i[2] for i in titles if i[1] not in duplicates]
urls = SET(urls)


while not download.lower() in ['y', 'n']:
    download = input('Invalid permission. Confirm download(s) (y/n)? ')
else:
    if download.lower() == 'y':
        for i in range(0, len(urls)):
            url = urls[i]
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                print('Downloaded', i+1, 'of', len(urls), vidinfo(urls[i]))
            except Exception:
                try:
                    print('Downloading to default Downloads folder')
                    with youtube_dl.YoutubeDL(ydl_opts2) as ydl:
                        info = ydl.extract_info(url, download=True)
                    print('Downloaded', i+1, 'of', len(urls), vidinfo(urls[i]))
                except Exception:
                    print('Unexpected error encountered while downloading and saving', i+1, 'of', len(urls))

                    print('Downloaded', len([i for i in urls if vidinfo(i) == 'N/A']), 'distinct new file(s)')
    else:
        print('Download(s) canceled')

# [print(i) for i in titles]
vid_thumbnails_list = [vidthumb(titles[i][2]) for i in range(len(titles))]

# [wb.open(i) for i in vid_thumbnails_list]

RR=[i for i in [[j[1], j[2].replace('watch?v=', 'embed/')] for j in titles]]
# print(RR)



############################    Displaying thumbnails and stuff    ############################

path = 'disp_vid_thumbnails.html' #rel_path

#DO NOT CHANGE `ORIG` -- This is the placeholder content
ORIG = r'''

        <p>
            
        </p>
		
		<iframe
			width="560" height = "340" frameborder="0" scrolling="no" id="iframe" title = "vid1"
			src="">
		</iframe>

'''

def reset_main():
    with open('all frames.txt', 'w', encoding = 'utf8') as f:
        f.write('')

reset_main()

def reset_placeholder():
    with open('add_frame.txt', 'w', encoding = 'utf8') as f:
        f.write(ORIG)

reset_placeholder()

def resetHTML():
    with open(path, 'w', encoding = 'utf8') as f:
        with open('resetHTML.html', 'r', encoding = 'utf8') as g:
            f.write(g.read())

def addInfo(title, url):
    global contt, a
    reset_placeholder()

    with open('add_frame.txt', 'r', encoding = 'utf8') as f:
        contt = (f.read())

    contt = (contt[:contt.find('<p>')+3] + title + contt[contt.find('</p>'):])
    contt = contt[:contt.find('src')+5] + url + contt[contt.find('src')+5:]

    with open('add_frame.txt', 'w+', encoding = 'utf8') as f:
        f.write(contt)

def divAdder(x):
    for i in x:
        # reset_placeholder()
        addInfo(i[0], i[1])

        #Add div to temp placeholder file -- "all frames.txt"
        with open('add_frame.txt', 'r', encoding = 'utf8') as f:
            contt = (f.read())

        div = contt[contt.find('/-->')+4 : contt.find('<!--*END*')]

        with open('all frames.txt', 'a', encoding = 'utf8') as f:
            f.write(div+'\n')

if download.lower() == 'y':
    resetHTML()

    divAdder(RR) #Add results to final html

    with open(path, 'r', encoding = 'utf8') as f:
        contt = f.read()

    with open('all frames.txt', 'r', encoding = 'utf8') as f:
        # print(f.read())
        f.seek(0)
        replaceWith = f.read()

    ss=contt.replace('**', replaceWith)

    with open(path, 'w', encoding = 'utf8') as f:
        f.write(ss)

    # print('Converting files to .wav')
    # for i in titles:
        #print(i[1])
        # convert_to_wav(Dpath, i[1]+'.mka')

    # Display the html file with video embeds
    os.chdir(curDir)

    # Newer Method [flask localhost server]
    try:
        if not os.path.isdir('templates'):
            os.mkdir('templates')
    except Exception:
        pass

    import shutil
    shutil.move(
        'disp_vid_thumbnails.html',
        'templates/disp_vid_thumbnails.html'
    )

    sp.Popen('py flask_main.pyw', shell = True)
    wb.open('http://localhost:5000')

    # Older Method [Python terminal localhost server] -- The newer method has no clear advantage over this method

    # sp.Popen('py -m http.server 78', shell=True)
    # wb.open('http://localhost:78/disp_vid_thumbnails.html')
