from pytube import YouTube

class log:
    def __init__(self, mode: bool=True) -> None:
        self.mode = mode
        
    def add_log(self, url:str):
        if self.mode:
            yt = YouTube(url)
            title = yt.title
            channel = yt.author
            views = yt.views
            fat = len(title)
            with open('info.log', 'a') as logs:
                logs.write(
                    f'''{"#"*fat}\n# Title: {title}\n# Channel: {channel}\n# Views: {views} Views\n{"#"*fat}\n\n
                    ''')