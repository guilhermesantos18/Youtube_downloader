import pytube

url = ''
yt = pytube.YouTube(url)
video = yt.streams.filter(only_audio=True).first()
video.download()
