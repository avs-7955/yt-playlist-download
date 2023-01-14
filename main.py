from pytube import Playlist, YouTube
import sys

# Path where the file will be saved.
path = "E:\Download\youtube_downloads"
link = sys.argv[1]

# Initializing playlist
playlist = Playlist(link)
print(f"Downloading the playlist: {playlist.title}\n")


def on_progress(vid, chunk, bytes_remaining):
    '''To display the progress bar and the details.'''
    current = ((vid.filesize - bytes_remaining)/vid.filesize)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    percentage_of_completion = (
        vid.filesize - bytes_remaining) / vid.filesize * 100
    totalsz = (vid.filesize/1024)/1024
    totalsz = round(totalsz, 1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    percentage_of_completion = round(percentage_of_completion, 1)
    sys.stdout.write(
        f'↳ |{status}| {percentage_of_completion}% Remaining:{remain} MB\r')
    sys.stdout.flush()


def complete(stream, path):
    '''To display the message after completion of download'''
    print("\nDownload completed!\n\n")


for url in playlist.video_urls:
    video = YouTube(url, on_progress_callback=on_progress,
                    on_complete_callback=complete)
    print("Title: ", video.title)
    print("Download has started.")
    video = video.streams.get_by_itag(137)
    video.download(f"{path}/{playlist.title[0:10]}")
