from yt_dlp import YoutubeDL

print("Welcome to the YouTube Video Downloader!")

# Get user inputs
url = input("Please enter the URL of the video or playlist you want to download: ")
quality = input("Please enter the desired quality (e.g., 'low', 'medium', 'high', 'best'): ")
destination = input("Please enter the destination folder (e.g., 'downloads'): ")

# Set options based on user input
if quality == "best":
    ydl_opts = {
        'format': 'best',  # Download the best quality available
        'outtmpl': f'{destination}/%(title)s.%(ext)s',  # Save in the specified folder
    }
elif quality == "low":
    ydl_opts = {
        'format': 'worstvideo+worstaudio/worst',  # Download the worst quality available
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
    }
elif quality == "medium":
    ydl_opts = {
        'format': 'best[height<=480]',  # Download medium quality (480p or lower)
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
    }
elif quality == "high":
    ydl_opts = {
        'format': 'best[height>=720]',  # Download high quality (720p or higher)
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
    }
else:
    print("Invalid quality selected. Defaulting to 'best'.")
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
    }

# Ask if the user wants to download a playlist or a single video
playlist_choice = input("Is this a playlist? (yes/no): ").strip().lower()
if playlist_choice == 'no':
    ydl_opts['noplaylist'] = True  # Download only the single video
else:
    ydl_opts['noplaylist'] = False  # Download the entire playlist

# Download the video
try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download completed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
