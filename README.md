

# YouTube-wav-Downloader

## Who needs this?

#### This project is primarily intended for music producers to allow them to easily download audios from YouTube videos, but anyone and everyone can use it for their personal work too.

## Why would you need this?

This is a simple *command line* tool that allows anyone to be able to download **audios-only** from YouTube videos.
#### I do understand that there are quite a few python libraries that allow you to download not only audios but videos also.
So for the sake of simplicity and ease of use, this program is dedicated to only download and/or search for YouTube videos for ready-to-use **audio-only .wav** files with user-experience in mind.

## Requirements

**This program has been tested on Windows OS only and will assume that you have Windows from here on.**

This program **may require** that you [download the 7zip archiving program](https://www.7-zip.org/) (This requirement **depends on availability** of .zip or .7z ffmpeg downloads - see next steps).

- This requires you to first [download ffmpeg from GyanDev](https://www.gyan.dev/ffmpeg/builds/) *(for Windows Only)*. The **ffmpeg essentials release** will suffice.

  ![image](https://user-images.githubusercontent.com/67545205/120630336-5ecaac80-c484-11eb-88b1-be4145354986.png)

  For detailed instructions on how to properly download ffmpeg watch this excellent video by TroubleChute on YouTube[![FFMPEG Download Instructions on YouTube by TroubleChute](https://user-images.githubusercontent.com/67545205/120638446-bde0ef00-c48d-11eb-8d30-ed01b699cdb6.png)](https://www.youtube.com/watch?v=r1AtmY-RMyQ).

- If the ffmpeg essentials download only has a **.7z** version and not a .zip, you will need to download the [**7zip** archiver](https://www.7-zip.org/) (zip/unzip tool).
  ![image](https://user-images.githubusercontent.com/67545205/120630598-9e919400-c484-11eb-96d6-55ce9e8c08f5.png)

- If you haven't already, you will need to install [**python**](https://www.python.org/), preferably the [latest version](https://www.python.org/downloads/). You can also [download python 3.9.5 (Latest version at the time of writing)](https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe).

  **Note that Python 3.9+ *cannot* be used on Windows 7 or earlier.**
  **\*\*** If you are on **Windows 7 or earlier** you can still [**download python 3.8.10**](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe) or *anything above 3.6* and expect full functionality.

  ### Note: On Installation, make sure to enable the `Add python to path` option for whatever version you are installing.

  ![1_add_python_to_path](res/py/1_add_python_to_path.png)

- After this, you need to install some *"python packages"*.
  This is very easy, you just need to enter `pip install -r requirements.txt` in **cmd**.
  **cmd** or **command prompt** is a preinstalled application on Windows OS systems.

  **To open cmd**, use the shortcut `⊞ Win` +`R`, type `cmd` in the dialog box and hit enter.
  
   ![Image - How to open cmd](res/cmd_runbox.png)

#### When opened, cmd looks like this
<img src="https://user-images.githubusercontent.com/67545205/120892187-9f642a80-c62a-11eb-8170-2feaf0147f88.png" alt="cmd_vs_powershell" width="3000">

- **Note: After running the** `pip install -r requirements.txt` **you'll be greeted with a looong installation, don't mind, keep waiting and continue once done!**


## Features
1. You can download audio from **any** YouTube URL you want.
2. You can download audios from **multiple** YouTube video URLs at once.
3. You can use the simple built in **text-based YouTube search** to search and download videos you like.
4. Any **duplicate files** will automatically be detected and will NOT be downloaded.
5. *New:* You can now download all songs from **Playlists on YouTube Music**
6. *New:* You can now download YouTube audios by adding urls to **separate "urls.txt" file** instead of writing typing out each one [Explained Later]
7. *New:* You can now download songs from Spotify (**\*accuracy may be less**) [NEEDS SPOTIFY API CREDENTIALS!] [Learn more](#method-5-of-5-download-songs-from-spotify-playlists)
8. After confirming downloads, you will be shown the selected downloaded videos **in your browser**.

**Note: Downloaded videos are always converted to `.wav` format**

## Usage Instructions
1. **Make sure all requirements are satisfied before starting with this program.**
2. When cmd opens up, type the path to the folder where this project's files are downloaded.
   **E.g.** If you have downloaded the files in the folder **youtube_downloader** in the location 
   **C:\Users\Vivo Jay\Downloads** you will need to do the following:
   Type `cd "C:\Users\Vivo Jay\Downloads"` and hit enter (Double quotes are required).
   ![image](https://user-images.githubusercontent.com/67545205/121413230-1d099c80-c983-11eb-9285-4849e89eff14.png)

3. Type `pip` and then `py --version` and check if they work\
   \
   ![image](https://user-images.githubusercontent.com/67545205/121410804-981d8380-c980-11eb-87a5-2290890d184f.png)
  
   We DON'T want this (If this happens, you must **REINSTALL PYTHON [See in "Requirements"]**):\
   ![image](https://user-images.githubusercontent.com/67545205/121412391-4970e900-c982-11eb-8b9b-34703619118c.png)


4. Now, type `pip install -r -requirements.txt` [See from Heading "Requirements"]
   **You don't need to do this again if you have done it once.**
   ![image](https://user-images.githubusercontent.com/67545205/121412895-ca2fe500-c982-11eb-9b03-d917c1b78807.png)

5. Just to check if installations have been successful, type `py download.py` and hit enter, if it shows `Error: No parameters entered, exiting...`, then it means **the program is working fine**.
   ![image](https://user-images.githubusercontent.com/67545205/121412602-84731c80-c982-11eb-8dcb-ceb62abadf59.png)

6. **Now you are ready to actually run the program**. To start downloading audio, there are **five methods.** Choose from below

## Choose your download method:
- [Download from URLs](#method-1-of-5-download-from-url)
- [Search and Download](#method-2-of-5-search-and-download)
- [Download using text file](#method-3-of-5-download-urls-from-text-file)
- [Download Playlists from YouTube Music](#method-4-of-5-download-playlists-from-youtube-music)
- *New* [Download songs from Spotify Playlists](#method-5-of-5-download-songs-from-spotify-playlists)
\
&nbsp;
## Method 1 of 5 [Download from URL]:
#### Enter one or multiple URLs in double quotes separated by a space after `py download.py`. For example if you want to download audios from the following URLs:
  - https://www.youtube.com/watch?v=RT5pYfOavkA
  - https://www.youtube.com/watch?v=7XcuZ8wZ3BY
  - https://www.youtube.com/watch?v=2qYLxw0Knu4

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The final command looks like this:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`py download.py "https://www.youtube.com/watch?v=RT5pYfOavkA" "https://www.youtube.com/watch?v=7XcuZ8wZ3BY" "https://www.youtube.com/watch?v=2qYLxw0Knu4"`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you want to download a single URL just type that in the double quotes instead as follows:
`py download.py "https://www.youtube.com/watch?v=RT5pYfOavkA"`

Then it asks you where you want to save the file.
Here, you can either:

- Enter/paste the path you want OR
- Don't type anything and just hit enter to **automatically** download in the **default Downloads** folder

### **Here's a detailed guide on how to download audios**

#### Add single URL or multiple URLs separated by spaces
![1_PS_Multi_URLs.png](res/PS/1_PS_Multi_URLs.png)

#### Next it prompts you to enter a path to save to
![2_PS_Enter_Path_On_Prompt.png](res/PS/2_PS_Enter_Path_On_Prompt.png)

#### You can enter a path manually or copy-paste
![3_PS_Enter_Any_Path_You_Want.png](res/PS/3_PS_Enter_Any_Path_You_Want.png)

#### Selected videos will be displayed in a table like this
![4_PS_Tabular_Results.png](res/PS/4_PS_Tabular_Results.png)

### After you confirm, your downloads will start shortly
![5_PS_Downloads_Started.png](res/PS/5_PS_Downloads_Started.png)

**Now the downloaded files are converted to wav files for easy use in your [DAW](https://en.wikipedia.org/wiki/Digital_audio_workstation)**
![6_PS_Converts_To_wav.png](res/PS/6_PS_Converts_To_wav.png)

### After confirming downloads, the selected audios will open in your browser
![7_PS_HTML_Showing_Selected_Audios.png](res/PS/7_PS_HTML_Showing_Selected_Audios.png)

#### You may also enter a save location before entering URLs at the start (optional)
![8_PS_Enter_Path_In_The_Beginning.png](res/PS/8_PS_Enter_Path_In_The_Beginning.png)

#### This program detects duplicate downloaded files also
![9_PS_Duplicates.png](res/PS/9_PS_Duplicates.png)

#### It always asks you for confirmation before downloads and you can cancel downloads if you wish
![10_PS_Cancel_Downloads.png](res/PS/10_PS_Cancel_Downloads.png)

## Method 2 of 5 [Search and Download]:
#### If you want to search for a video and then download it, just type `py download.py s` followed by the search terms (without double quotes this time).
  **E.g.** If you want to search for "lolo zouai moi lyric video" then type the following command:
  `py download.py s lolo zouai moi lyric video`

**In cmd it looks like this**
![11_PS_Search_For_YouTube_Vids.png](res/PS/11_PS_Search_For_YouTube_Vids.png)

#### Here you have the option to select one or more search results
- **To select a video just type the number given next to it**
- **To select a multiple videos type the video numbers separated by spaces**![12_PS_Search_Results_Select_Multiple.png](res/PS/12_PS_Search_Results_Select_Multiple.png)

#### Just like before, enter the path you would like to save the audio(s) to
![13_PS_Enter_Path_Just_Like_Before.png](res/PS/13_PS_Enter_Path_Just_Like_Before.png)

#### Note that if you leave the save location empty, it will automatically save to the Default Download Path
![14_PS_Download_In_Default_Downloads_Directory](res/PS/14_PS_Download_In_Default_Downloads_Directory.png)

#### The selected audios will be displayed in a table
![15_Shows_Multiple_Search_Selections.png](res/PS/15_Shows_Multiple_Search_Selections.png)

#### As always, the selected audios will open in your browser once you confirm your downloads
![Videos_Selections_On_Browser](res/Videos_Selections_On_Browser.png)

### You will now be able to see the downloaded audios where you saved them
![Files_In_Explorer](res/Files_In_Explorer.png)

## Method 3 of 5 [Download URLs from text file]:
### This provides you an **easier** way to enter URLs.
  How does it work?
  Instead of entering URLs in the terminal directly, you can now add them in a text file in *separate lines* and save it in **"urls.txt"**.
  
  **Important Note:**
  **Make sure to create this file in this project's folder**
  So if you have downloaded the project as **C:\Users\VivoJay\Downloads\YouTube-wav-Downloader** then you need to create the file in that SAME folder.
  \
  \
  \
  **This This is an example of how the file "urls.txt" may look like:**

  ![image](https://user-images.githubusercontent.com/67545205/120674230-871cd000-c4b1-11eb-8c6d-6b15ba05ad09.png)

  Now to download audios from this file, just type `py download.py urls`.
  
#### This is all you need to type
  ![image](https://user-images.githubusercontent.com/67545205/120675442-b2ec8580-c4b2-11eb-80ba-f61a0af15264.png)

#### Choose a download path and continue as usual
  ![image](https://user-images.githubusercontent.com/67545205/120675532-c8fa4600-c4b2-11eb-91f1-3ac53f1f72ff.png)

## Method 4 of 5 [Download Playlists from YouTube Music]:
#### To download YouTube Music playlists, all you need to do is add their links to a txt file named **"yt_playlists.txt"** in **this project's folder**.
  So if you have downloaded the project as **C:\Users\VivoJay\Downloads\YouTube-wav-Downloader** then you need to create the file in that SAME folder.
  Now in this file, add the YouTube Music Playlist URLs in *separate lines*.
  \
  \
  **This is an example of how the file "yt_playlists.txt" may look like:**
  
  ![image](https://user-images.githubusercontent.com/67545205/120677771-0e1f7780-c4b5-11eb-94aa-5c8fecc33276.png)

#### This is all you need to type in cmd
  ![image](https://user-images.githubusercontent.com/67545205/120678801-1f1cb880-c4b6-11eb-8915-60acebbcd15b.png)
  **Note:** This can take some time!

#### After this you can continue downloading as usual
  ![image](https://user-images.githubusercontent.com/67545205/120679673-124c9480-c4b7-11eb-92ee-645cc27456c4.png)
#### The Playlists will be loaded and you'll their name and author
  ![image](https://user-images.githubusercontent.com/67545205/120679946-5fc90180-c4b7-11eb-8140-eba460ab13b4.png)

## Method 5 of 5 [Download songs from Spotify Playlists]:

### This requires you to register on developers.spotify.com as a developer and get your "SPOTIFY API KEY"
If you are NOT familiar with this, you can leave this method. This method delves into a bit more advanced stuff than the rest of this program.

Anyways, if you want a quick start, view this small and quick ["BASIC TUTORIAL"](#extras---spotify-developers-tutorial) and come back here once you're done.

### Simple guide on **How to find spotify playlist URIs** given later. . .
### This method is similar to Method 4:
#### To download spotify playlists, all you need to do is add their links to a txt file named **"spot_playlists.txt"** in **this project's folder**.
  So if you have downloaded the project as **C:\Users\VivoJay\Downloads\YouTube-wav-Downloader** then you need to create the file in that SAME folder.
  Now in this file, add the YouTube Music Playlist URLs in *separate lines*.
  \
  \
  **This is an example of how the file "spot_playlists.txt" may look like:**
  ![image](https://user-images.githubusercontent.com/67545205/121406579-ef6d2500-c97b-11eb-8aaa-730dbad8a8fc.png)
  #### The playlists tracks will now be loaded one-by-one
  
  Now to download audios from this file, just type `py download.py spot` and the songs from your selected Spotify Playlist will start loading.
  ![image](https://user-images.githubusercontent.com/67545205/121406858-4d9a0800-c97c-11eb-894d-5563e41d5f04.png)
  **Note:** This can take some time!
  ![image](https://user-images.githubusercontent.com/67545205/121407130-9d78cf00-c97c-11eb-843c-ae53a866800a.png)

  Download where you wish
  ![image](https://user-images.githubusercontent.com/67545205/121407417-e92b7880-c97c-11eb-880b-cf162177c456.png)
  **Now continue normally, the program will guide you**



### Right click on the playlist, go to `Share`, select `Copy link to Playlist`
![Selecting_Playlist_URI](https://user-images.githubusercontent.com/67545205/121406187-7bcb1800-c97b-11eb-9bcd-9b869dbde24a.png)


## Extras - Spotify Developers Tutorial
1. Visit the [Spotify Dashboard](https://developer.spotify.com/dashboard/login) and sign up.
   ![image](https://user-images.githubusercontent.com/67545205/121416516-84751b80-c986-11eb-9f22-a9363342d89e.png)
2. Accept their terms
   ![image](https://user-images.githubusercontent.com/67545205/121416846-e6358580-c986-11eb-8683-a88af3a7f4d2.png)
3. Click "Create an App"
   ![image](https://user-images.githubusercontent.com/67545205/121416902-f77e9200-c986-11eb-9e8c-40a2047da8a9.png)
4. Name it whatever you want (E.g. "Cool App"), tick the checkboxes, add any description and hit "create"
   ![image](https://user-images.githubusercontent.com/67545205/121417002-12510680-c987-11eb-8de7-c069e561023a.png)
5. NEVER share your "Client ID" or "Client Secret" with anyone (Not even yourself \s)
   ![image](https://user-images.githubusercontent.com/67545205/121417402-7c69ab80-c987-11eb-87db-b49d53359777.png)
6. Use the `SET` command in cmd as follows:
   If your Client ID is `99999999999999999999aaaaaaaaaaaa` and
   your Client Secret is `11111111111111111111bbbbbbbbbbbb`, then:
   
   Open the commands prompt and type the following commands [Replace these with your own ID and Secret]:
   - `SET SPOT_CLIENT_ID=99999999999999999999aaaaaaaaaaaa`
   - `SET SPOT_CLIENT_SECRET=11111111111111111111bbbbbbbbbbbb`
   
   After this, you are set to start downloading your own Spotify Playlist Tracks, [go here](#method-5-of-5-download-songs-from-spotify-playlists)
