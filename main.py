from argparse import ArgumentParser
from youtube import downtube, fix_bug
from banner.banner import banner

if __name__ == '__main__':
    # fix bug cipher
    arquivo = ''
    fixing = fix_bug()
    fixing.fix_cipher(path=arquivo, line=410, new_line='teste')
    
    # CLI
    parser = ArgumentParser(description='teste')
    parser.add_argument('--video', help='Download Video From YouTube')
    parser.add_argument('--audio', help='Download Audio From YouTube')
    parser.add_argument('--playlist', help='Download a Playlist From YouTube')
    arg = parser.parse_args()
    arg_video = arg.video
    arg_audio = arg.audio
    arg_playlist = arg.playlist
    
    banner()
    downTube = downtube(internet_check=True)
    if arg_video:
        downTube.download_video(arg_video)
    if arg_audio:
        downTube.download_audio(arg_audio)
    if arg_playlist:
        downTube.download_playlist(arg_playlist)