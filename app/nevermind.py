from pytube import YouTube
import vlc
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams.first()
Player=vlc.Instance()
