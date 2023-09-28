from pytube import YouTube, Playlist
from rich.progress import track
import requests, sys

C = '\033[36m' # cyan
W = '\033[0m'  # white 
G = '\033[32m' # green
O = '\033[33m' # orange

class fix_bug:
    def __init__(self, active_fix:bool=False) -> None:
        self.active_fix = active_fix
        
    def fix_cipher(self, path: str, line: int, new_line: str):
        if self.active_fix != False:
            with open(path, 'r') as cipher:
                text = cipher.readlines()

            with open(path, 'w') as cipher:
                for i in text:
                    if text.index(i) == line:
                        cipher.write(f'''    transform_plan_raw = js''')
                    else:
                        cipher.write(i)
class downtube:
    def __init__(self, internet_check:bool=True) -> None:
        self.check = internet_check
        
    def on_progress(self, streams, chunk: bytes, bytes_remaining: int):
        contentsize = self.video.filesize
        size = contentsize - bytes_remaining    
        print('\r' + '› [ Downloading ]:[%s%s] %.2f%%;' % ('█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
        
    def __check_network(self):
        if self.check:
            try:
                requests.get('http://google.com', timeout=5)
                return True
            except requests.ConnectionError:
                return False

    def __check(self):
        if self.__check_network() is not None:
            if self.__check_network() != True:
                print('network error')
                sys.exit()
            
    def download_video(self, url:str):
        self.__check()        
        if url is not None:
            if 'https' in url:
                try: 
                    yt = YouTube(url, on_progress_callback=self.on_progress)
                    self.video = yt.streams.get_highest_resolution()
                    self.video.download('video')
                except Exception as e:
                    print('[!] [red]Download Error[/]')
            else:
                print(f'{W}exemple usage: {G}python3 {W}main.py {C}--video {O}https://youtu.be/9PnEtt4qFxY?si=ZJHMkDCoXVkvOLTN[/]')
                    
    def download_audio(self, url:str):
        self.__check()
        if url is not None:
            if 'https' in url:
                try: 
                    yt = YouTube(url, on_progress_callback=self.on_progress)
                    self.video = yt.streams.get_by_itag(251)
                    self.video.download('audio')
                except Exception as e:
                    print('[!] [red]Download Error[/]')
            else:
                print(f'{W}exemple usage: {G}python3 {W}main.py {C}--audio {O}https://youtu.be/9PnEtt4qFxY?si=ZJHMkDCoXVkvOLTN[/]')
    
    def download_playlist(self, url:str):
        self.__check()
        if url is not None:
            if 'playlist?' in url:
                try:
                    yt_playlist = Playlist(url)
                    for v_playlist in track(yt_playlist.videos, 'Downloading Playlist'):
                        playlist = v_playlist.streams.get_highest_resolution()
                        playlist.download('playlist')
                except:
                    print('[!] [red]Download Error[/]')
            else:
                print(f'{W}exemple usage: {G}python3 {W}main.py {C}--playlist {O}https://youtu.be/9PnEtt4qFxY?si=ZJHMkDCoXVkvOLTN[/]')