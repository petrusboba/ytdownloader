import pygame
import youtube_dl
from youtube_search import YoutubeSearch

YOUTUBE_API_KEY = "AIzaSyC84eBTkhnTWGtVOXJ-HClCZDyxPnmXliI"  # Ganti dengan API key Anda

def search_youtube(query):
    results = YoutubeSearch(query, max_results=1).to_dict()
    if results:
        video_id = results[0]['id']
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        print("Tidak dapat menemukan lagu.")
        return None

def download_song(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'verbose': True,
        'nocheckcertificate': True,
        'ignoreerrors': True
    }

    video_url = search_youtube(query)
    if video_url:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(video_url, download=False)
                title = info['title']
                ydl.download([video_url])
                return f"{title}.mp3"
            except youtube_dl.utils.DownloadError as e:
                print(f"Error downloading song: {e}")
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

def play_song(song_path):
    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

if __name__ == "__main__":
    query = input("Masukkan judul lagu: ")
    song_path = download_song(query)
    
    if song_path:
        play_song(song_path)
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print("Tidak dapat mendownload lagu.")
