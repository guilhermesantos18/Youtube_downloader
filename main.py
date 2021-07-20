import pytube

# Download em formato mp4
url = input('Url musica que deseja fazer o download: ')
yt = pytube.YouTube(url)
video = yt.streams.filter(only_audio=True).first()
destino = input('Digite o endereço da pasta que deseja guardar a música: ')
ficheiro_music = video.download(output_path=destino)
