from pytube import YouTube
from tkinter import filedialog

yt=YouTube('https://youtu.be/nwRoHC83wx0')
#print('Video Title ->',yt.title)
#print('Views ->',yt.views)
#print('YouTube Channel ->',yt.author)
#print('Description Box ->',yt.description)
print(yt.streams)
for i in yt.streams:
    print(i)

all_streams=yt.streams
p240=all_streams.filter(resolution='240p'.last())
print('Downloading.......Please Wait')
location=filedialog.askdirectory()
p720.download(output_path=str(location),filename='Gayatri Mantra.mkv')
print(f'{yt.title} Download Complete')
