from flask import Flask, request, send_file
from flask.helpers import send_from_directory
from flask_cors import CORS
import json
from yt_dlp import YoutubeDL
import os


app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

root = os.getcwd()
execs = root + "\executables"
songs = root + "\song_files"
whisper = execs + "\whisper"

#Download and separation of audio
@app.route("/script", methods=["GET", "POST"])
def script():
    language = request.args.get('lang')
    url = request.args.get('url')
    os.chdir(root)
    URLS = [url]
    with YoutubeDL() as ydl:
        info = ydl.extract_info(URLS[0], download=False)
        title = info["title"]
        identifier = info["id"]
        filename = title + " [" + identifier + "]"
        filename = f'{filename.title()}.webm'

    return title + "|" + "Done"

#Route to video
@app.route('/video/<song_name>')
def serve_video(song_name):
    video_folder = os.path.join(songs, song_name)
    video_files = [f for f in os.listdir(video_folder) if f.endswith(".webm")]
    if len(video_files) == 0:
        return "Video not found"
    return send_file(os.path.join(video_folder, video_files[0]), mimetype='video/webm')

#Route to all videos
@app.route('/video')
def serve_name():
    song_names = []
    for file_name in os.listdir(songs):
        song_names.append(file_name)
    return json.dumps({"song_names": song_names})

#Backend defined to use production build
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()