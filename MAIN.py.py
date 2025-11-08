import yt_dlp
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import shutil
### run this code using mobile phone youtube videolink.


# Check FFmpeg
def check_ffmpeg():
    #  system PATH
    if shutil.which("ffmpeg"):
        return shutil.which("ffmpeg")
    
    possible_path = r"C:\ffmpeg\ffmpeg-8.0-essentials_build\bin"
    if os.path.exists(possible_path):
        return possible_path
    return None

FFMPEG_PATH = check_ffmpeg()
if not FFMPEG_PATH:
    messagebox.showwarning("FFmpeg Missing", "FFmpeg not found! Please install FFmpeg and add it to PATH.")

# Download function
def download_video(url, save_path, progress_var, status_label):
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = float(d.get('_percent_str', '0.0').replace('%',''))
            progress_var.set(percent)
            status_label.config(text=f"Downloading: {d.get('_percent_str','0%')} at {d.get('_speed_str','0B/s')} ETA {d.get('_eta_str','0s')}")
        elif d['status'] == 'finished':
            progress_var.set(100)
            status_label.config(text="Download complete!")

    if not FFMPEG_PATH:
        messagebox.showerror("FFmpeg Error", "FFmpeg is required for downloading bestvideo+bestaudio.")
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'noplaylist': True,
        'retries': 10,
        'continuedl': True,
        'ffmpeg_location': FFMPEG_PATH,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        messagebox.showerror("Download Failed", f"Error: {e}")

# Thread wrapper to avoid GUI freeze
def start_download(url_entry, folder_var, progress_var, status_label):
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return
    save_path = folder_var.get() or '.'
    threading.Thread(target=download_video, args=(url, save_path, progress_var, status_label), daemon=True).start()

# Folder selection
def browse_folder(folder_var):
    path = filedialog.askdirectory()
    if path:
        folder_var.set(path)

# GUI Setup
root = tk.Tk()
root.title("Modern YouTube Downloader")
root.geometry("600x320")
root.resizable(False, False)

# URL Entry
tk.Label(root, text="YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=70)
url_entry.pack(pady=5)

# Folder Selection
folder_var = tk.StringVar()
tk.Label(root, text="Save Folder:").pack(pady=5)
folder_frame = tk.Frame(root)
folder_frame.pack(pady=5)
folder_entry = tk.Entry(folder_frame, textvariable=folder_var, width=50)
folder_entry.pack(side=tk.LEFT, padx=5)
tk.Button(folder_frame, text="Browse", command=lambda: browse_folder(folder_var)).pack(side=tk.LEFT)

# Progress Bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=400)
progress_bar.pack(pady=15)

# Status Label
status_label = tk.Label(root, text="Status: Waiting...", anchor="w")
status_label.pack(fill="x", padx=20)

# Download Button
tk.Button(root, text="Download Video", command=lambda: start_download(url_entry, folder_var, progress_var, status_label),
          bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()
