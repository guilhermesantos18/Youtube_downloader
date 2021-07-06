import pytube
import os

url = input('Url musica que deseja fazer o download: ')
yt = pytube.YouTube(url)
video = yt.streams.filter(only_audio=True).first()
destino = input('Digite o endereço da pasta que deseja guardar a música: ')
ficheiro_music = video.download(output_path=destino)
# Remove a extensão mp4
base, ext = os.path.splitext(ficheiro_music)
# Adiciona a extensão mp3
musica = base + '.mp3'
# Renomeia o ficheiro
os.rename(ficheiro_music, musica)
