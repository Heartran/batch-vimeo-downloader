import os 
import tempfile
import yt_dlp
from dotenv import load_dotenv

load_dotenv()

file_path = os.path.join(os.path.dirname(__file__), "vimeo_links.txt")
output_folder = os.getenv("FOLDER_PATH")
batch_size = 5

yt_dlp_options = {
    "format": "bestvideo+bestaudio",
    "referer": "CHANGE YOUR REFERER HERE",
    "external_downloader": "aria2c",
    "external_downloader_args": ["-x", "16", "-s", "16", "-k", "5M", "--max-concurrent-downloads=16"],
    "outtmpl": os.path.join(output_folder, "%(title)s (%(format_id)s).%(ext)s"),
    "clean_infojson": False,
    "nooverwrites": True,
    "verbose": True,
    "tempdir": tempfile.gettempdir(),
    "username": os.getenv("VIMEO_USERNAME"),
    "password": os.getenv("VIMEO_PASSWORD"),
}

os.makedirs(output_folder, exist_ok=True)

with open(file_path, "r") as file:
    video_lines = [line.strip() for line in file]

for i in range(0, len(video_lines), batch_size):
    batch_lines = video_lines[i:i + batch_size]
    ydl = yt_dlp.YoutubeDL(yt_dlp_options)

    for line in batch_lines:
        url, password = line.split("::") if "::" in line else (line, None)

        # Skip the video if it's already downloaded
        try:
            video_info = ydl.extract_info(url, download=False)
            output_file = ydl.prepare_filename(video_info)
            if os.path.exists(output_file):
                print(f"Il file '{output_file}' esiste già. Skipping...")
                continue
        except Exception as e:
            print(f"Errore nel controllo del file già scaricato per {url}: {e}")
            continue

        ydl.params['videopassword'] = password
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Errore nel download di {url}: {e}")
            if "404" in str(e):
                print("Il video potrebbe essere stato rimosso o reso privato.")
        except Exception as e:
            print(f"Errore generico nel download di {url}: {e}")

for file_name in os.listdir(output_folder):
    file_path = os.path.join(output_folder, file_name)
    if os.path.isfile(file_path) and not file_name.lower().endswith(".mp4"):
        os.remove(file_path)
