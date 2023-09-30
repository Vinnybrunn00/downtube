from argparse import ArgumentParser
from youtube import downtube
from banner.banner import banner
from logs import log

if __name__ == '__main__':
    
    # CLI
    parser = ArgumentParser(description='This script, written in Python, is capable of downloading videos, audios (music) and playlists from YouTube in high quality for free.')
    parser.add_argument('--video', help='Download Video From YouTube')
    parser.add_argument('--audio', help='Download Audio From YouTube')
    parser.add_argument('--playlist', help='Download a Playlist From YouTube')
    arg = parser.parse_args()
    arg_video = arg.video
    arg_audio = arg.audio
    arg_playlist = arg.playlist
    
    logs = log()
    banner()
    downTube = downtube(internet_check=True)
    if arg_video:
        downTube.download_video(arg_video)
        logs.add_log(arg_video)
    if arg_audio:
        downTube.download_audio(arg_audio)
        logs.add_log(arg_audio)
    if arg_playlist:
        downTube.download_playlist(arg_playlist)