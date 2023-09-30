# DownTube

This script, written in Python, is capable of downloading videos, audios (music) and playlists from YouTube in high quality for free. The script is compatible on any system.

<div align="center">
  <a href="https://instagram.com/vinnybrunn00" target="_blank"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" target="_blank"></a>
  <a href="https://twitter.com/Vinnybrunn00" target="_blank"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white"></a>
  <a href="https://open.spotify.com/user/5cuqma0170zaestki4kbc1ilp?si=bf30147a1b2a4978" target="_blank"><img src="https://img.shields.io/badge/tmux-1BB91F?style=for-the-badge&logo=tmux&logoColor=white"></a>
  <a href="https://open.spotify.com/user/5cuqma0170zaestki4kbc1ilp?si=bf30147a1b2a4978" target="_blank"><img src="https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white"></a>
  <a href="https://instagram.com/vinnybrunn00" target="_blank"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=black" target="_blank"></a>
</div>

## Installation
- Cloning Repository and Accessing the Folder
```bash
$ git clone https://github.com/Vinnybrunn00/downtube.git
```

```bash
$ cd downtube
```

- Installing Dependencies
```bash
$ pip install -r requirements.txt
```

## Usage
``` bash
 $ python3 main.py --help                                                                                             
usage: main.py [-h] [--video VIDEO] [--audio AUDIO] [--playlist PLAYLIST]

This script, written in Python, is capable of downloading videos, audios (music) and playlists from YouTube in high quality for
free.

options:
  -h, --help           show this help message and exit
  --video VIDEO        Download Video From YouTube
  --audio AUDIO        Download Audio From YouTube
  --playlist PLAYLIST  Download a Playlist From YouTube
```
## Exemple
```bash
$ python3 main.py --video https://www.youtube.com/watch?v=xaCYvpcvHns
```
